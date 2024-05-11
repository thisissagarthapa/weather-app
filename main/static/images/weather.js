const apiKey="bc38b8094a1c19d34e0e1b479d8e5e15";
const apiUrl="https://api.openweathermap.org/data/2.5/weather?q=&appid=bc38b8094a1c19d34e0e1b479d8e5e15&units=standard";

const searchBox=document.querySelector(".search  input");
const searchBtn=document.querySelector(".search button");
async  function checkWeather(city){
    const response= await fetch(apiUrl+ city+`appid=${apiKey}`)
    var data= await response.json();
    console.log(data);
    document.querySelector(".city").innerHTML=data.name

    document.querySelector(".temp").innerHTML=data.main.temp

    document.querySelector(".humidity").innerHTML=data.main.humidity

    document.querySelector(".wind").innerHTML=data.wind.speed
    searchBtn.addEventListener(click,()=>{
        checkWeather(searchBox.value);
    })

}


