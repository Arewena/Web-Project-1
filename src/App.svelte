<script>
    let name = "닉네임:"
    let tier = "티어:"
    let kda = "평균 KDA:"
    let vision = "평균 시야점수:"
    let killRate = "평균 킬관여율:"
    let cs = "평균 cs:"
    let deathPerDamage = "데스 당 딜량:"
  
    fetch("http://127.0.0.1:8000/info").then((response) => {
      response.json().then((json) => {
        name = json.name;
        tier = json.tier;
        kda = json.kda;
        vision = json.vision;
        killRate = json.killRate;
        cs = json.cs;
        deathPerDamage = json.deathPerDamage;


      });
    });
  </script>
  
  

<nav class="123">
  <div>
    <ul class="contain">
      <!-- svelte-ignore a11y-missing-attribute -->
      <li class="item"><a herf="">사진을 위한 공백</a></li>
      <!-- svelte-ignore a11y-missing-attribute -->
      <li class="item"><a herf="">About Me</a></li>
      <!-- svelte-ignore a11y-missing-attribute -->
      <li class="item"><a herf="">Project 1</a></li>
      <!-- svelte-ignore a11y-missing-attribute -->
      <li class="item"><a herf="">Project 2</a></li>
      <!-- svelte-ignore a11y-missing-attribute -->
      <li class="item"><a herf="">Project 3</a></li>
    </ul>
  </div>
  
  <button class="left"></button>
  
  <input class="left" type="text" id="user_id" placeholder="비교할 플레이어의 닉네임을 입력하세요." />
  <button class="right"></button>
  <input class="right" type="text" id="user_id" placeholder="비교할 플레이어의 닉네임을 입력하세요." />
  <h1>&nbsp;</h1>
  <h1>&nbsp;</h1>

  <h1>{name}</h1>
  <h1>{tier}</h1>
  <h1>{kda}</h1>
  <h1>{vision}</h1>
  <h1>{killRate}</h1>
  <h1>{cs}</h1>
  <h1>{deathPerDamage}</h1>

</nav>



