from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import requests
import json
from urllib import parse
import time

token = ''

url1 = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + parse.quote("T1 Gumayusi")
response = requests.get(url1, headers={'X-Riot-Token': token})

url2 = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + response.json()['id']
response2 = requests.get(url2, headers={'X-Riot-Token': token})

puuid = response.json()['puuid']
app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/info")
async def root():
    if response.status_code == 200:
        #변수 초기화1
        information = json.loads(response2.text)[0]
        #티어
        nickname = information['tier'][0] + information['tier'][1:].lower()
        #세부 랭크(숫자)
        number = 0
        if information['rank'] == "IV": number = 4
        elif information['rank'] == "III": number = 3
        elif information['rank'] == "II": number = 2
        else: number = 1
        name = response.json()["name"]
        gameId = requests.get(f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids",headers={'X-Riot-Token': token}).json()
        k, d, a = 0, 0, 0
        visionScore = 0
        averageKilRate = []
        deathPerDamage = []
        averageCS = []

        for i in gameId:
            #변수 초기화2
            gameData = requests.get(f"https://asia.api.riotgames.com/lol/match/v5/matches/{i}",headers={"X-Riot-Token": token}).json()
            playerwin = True
            winTeamKills, loseTeamKills = 0, 0
            targetKills, targetAssists = 0, 0
            csPerMinuite = 0

            for j in gameData['info']['participants']:
                # 블루팀 레드팀 킬 나누기(bk가 블루팀이라는건 보장하지 않지만, 나누기만 하면 장땡)
                if j['win']: winTeamKills += j['kills']
                else: loseTeamKills += j['kills']

                if j['summonerName'].lower() == name.lower():
                    #이겼는지 여부
                    playerwin = j['win']
                    #평균 cs
                    csPerMinuite = round((j['totalMinionsKilled'] + j['neutralMinionsKilled']) / round((gameData['info']['gameDuration'] / 60), 1), 1)
                    #킬관여율
                    targetKills += j['kills']
                    targetAssists += j['assists']
                    #KDA
                    k += j['kills']
                    d += j['deaths']
                    a += j['assists']
                    #시야점수
                    visionScore += j['visionScore']
                    #데스 당 딜량
                    try:
                        deathPerDamage.append(round(j['totalDamageDealtToChampions'] / j['deaths']))
                    except:
                        deathPerDamage.append(j['totalDamageDealtToChampions'])
            #평균 cs append
            averageCS.append(csPerMinuite)

            #승리팀일시 winTeam으로, 패배팀일시 loseTeam로
            if playerwin:
                # 0/n/0박았을시 에러나기때문에 try 사용
                try:
                    averageKilRate.append(round((targetKills + targetAssists) / winTeamKills, 2) * 100)
                except:
                    averageKilRate.append(0)
            else:
                try:
                    averageKilRate.append(round((targetKills + targetAssists) / loseTeamKills, 2) * 100)
                except:
                    averageKilRate.append(0)
            time.sleep(0.4)

        return {"name": "닉네임: {}".format(response.json()["name"]),
                "tier": f"티어: {nickname} {number}",
                "kda": f"평균 KDA: {round((k + a ) / d, 2)}",
                "vision": f"평균 시야점수: {visionScore/ 20}",
                "killRate": f"평균 킬관여율: {round(sum(averageKilRate) / len(averageKilRate))}%",
                "cs" : f"평균 cs: {round(sum(averageCS) / len(averageCS), 1)}",
                "deathPerDamage": f"데스 당 딜량: {round(sum(deathPerDamage) / len(deathPerDamage))}"
                }
