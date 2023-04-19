<script>
  let name = "닉네임 :"
  let tier = "티어 :"
  let name2 = ": 닉네임"
  let tier2 = ": 티어"
  let inputNickName;
  let inputNickName2;

  let green_kda = "0";
  let green_vision = "0";
  let green_killRate = "0%";
  let green_cs ="0";
  let green_deathPerDamage = "0";
  let green_solokills = "0";

  let blue_kda = "0";
  let blue_vision = "0";
  let blue_killRate = "0%";
  let blue_cs ="0";
  let blue_deathPerDamage = "0";
  let blue_solokills = "0";

  const doRequest = async (nickname) => {
    const returnValue = await fetch("http://127.0.0.1:8000/api/first", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({name: nickname})

    })
    const data = await returnValue.json()
    name = data['name']
    tier = data['tier']
    
    green_kda = data['kda']
    green_vision = data['vision']
    green_killRate = data['killRate'] + "%"
    green_cs = data['cs']
    green_deathPerDamage = data['deathPerDamage']
    green_solokills = data['solokills']

    document.getElementById('green_1').style.width = (data['kda'] / 4.5 * 100) + "%";
    document.getElementById('green_2').style.width = (data['vision'] / 60 * 100) + "%";
    document.getElementById('green_3').style.width = data['killRate'] + "%";
    document.getElementById('green_4').style.width = (data['cs'] * 10) + "%";
    document.getElementById('green_5').style.width = (data['deathPerDamage'] / 10) + "%";
    document.getElementById('green_6').style.width = (data['solokills'] / 3 * 100) + "%";
    
  }
  const doRequest2 = async (nickname) => {
    const returnValue = await fetch("http://127.0.0.1:8000/api/second", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({name: nickname})

    })
    const data = await returnValue.json()
    name2 = data['name']
    tier2 = data['tier']

    blue_kda = data['kda']
    blue_vision = data['vision']
    blue_killRate = data['killRate'] + "%"
    blue_cs = data['cs']
    blue_deathPerDamage = data['deathPerDamage']
    blue_solokills = data['solokills']

    document.getElementById('blue_1').style.width = (data['kda'] / 4.5 * 100) + "%";
    document.getElementById('blue_2').style.width = (data['vision'] / 60 * 100) + "%";
    document.getElementById('blue_3').style.width = data['killRate'] + "%";
    document.getElementById('blue_4').style.width = (data['cs'] * 10) + "%";
    document.getElementById('blue_5').style.width = (data['deathPerDamage'] / 10) + "%";
    document.getElementById('blue_6').style.width = (data['solokills'] / 3 * 100) + "%";

  }

</script>



<nav class="123">
<div>
  <ul class="contain">
  </ul>
</div>

<button on:click={() => doRequest(inputNickName)} class="left"></button>
<input bind:value={inputNickName} class="left" type="text" id="user_id" placeholder="비교할 플레이어의 닉네임을 입력하세요." />

<button on:click={() => doRequest2(inputNickName2)} class="right"></button>
<input bind:value={inputNickName2} class="right" type="text" id="user_id" placeholder="비교할 플레이어의 닉네임을 입력하세요." />
<h1>&nbsp;</h1>

<div class="container">
  <h1>{name}</h1>
  <h1 class="right_contain">{name2}</h1>
</div>
<div class="container">
  <h1>{tier}</h1>
  <h1 class="right_contain">{tier2}</h1>
</div>
<h1>&nbsp;</h1>


<div class="container2">
  <div class="left_progress_bar_background">
    <div class="left_progress_bar" id="green_1"> </div>
  </div>
  <div class="sort2">
    <h1 class="textbox_green">{green_kda}</h1>
    <h1>KDA</h1>
    <h1 class="textbox_blue">{blue_kda}</h1>
  </div>
  <div class="right_progress_bar_background">
    <div class="right_progress_bar" id="blue_1"> </div>
  </div>
</div>

<div class="container2">
  <div class="left_progress_bar_background">
    <div class="left_progress_bar" id="green_2"> </div>
  </div>
  <div class="sort2">
    <h1 class="textbox_green">{green_vision}</h1>
    <h1>시야점수</h1>
    <h1 class="textbox_blue">{blue_vision}</h1>
  </div>
  <div class="right_progress_bar_background">
    <div class="right_progress_bar" id="blue_2"> </div>
  </div>
</div>

<div class="container2">
  <div class="left_progress_bar_background">
    <div class="left_progress_bar" id="green_3"> </div>
  </div>
  <div class="sort2">
    <h1 class="textbox_green">{green_killRate}</h1>
    <h1>킬 관여율</h1>
    <h1 class="textbox_blue">{blue_killRate}</h1>
  </div>
  <div class="right_progress_bar_background">
    <div class="right_progress_bar" id="blue_3"> </div>
  </div>
</div>

<div class="container2">
  <div class="left_progress_bar_background">
    <div class="left_progress_bar" id="green_4"> </div>
  </div> 
  <div class="sort2">
    <h1 class="textbox_green">{green_cs}</h1>
    <h1>분 당 cs</h1>
    <h1 class="textbox_blue">{blue_cs}</h1>
  </div>
  <div class="right_progress_bar_background">
    <div class="right_progress_bar" id="blue_4"> </div>
  </div>
</div>

<div class="container2">
  <div class="left_progress_bar_background">
    <div class="left_progress_bar" id="green_5"> </div>
  </div>
  <div class="sort2">
    <h1 class="textbox_green">{green_deathPerDamage}</h1>
    <h1>분 당 딜량</h1>
    <h1 class="textbox_blue">{blue_deathPerDamage}</h1>
  </div>
  <div class="right_progress_bar_background">
    <div class="right_progress_bar" id="blue_5"> </div>
  </div>
</div>

<div class="container2">
  <div class="left_progress_bar_background">
    <div class="left_progress_bar" id="green_6"> </div>
  </div>
  <div class="sort2">
    <h1 class="textbox_green">{green_solokills}</h1>
    <h1>평균 솔로 킬</h1>
    <h1 class="textbox_blue">{blue_solokills}</h1>
  </div>
  <div class="right_progress_bar_background">
    <div class="right_progress_bar" id="blue_6"> </div>
  </div>
</div>
</nav>
