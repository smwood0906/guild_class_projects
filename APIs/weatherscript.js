$.ajax({

    url: "http://api.openweathermap.org/data/2.5/weather?q=" + "Portland,OR" + "&appid=1fcda43fd969332cca2ca765913b4481",
    method: 'GET',
    success: function (data) {
        console.log(data);
        console.log($("#location").html(data.name));
        var displayTemp = $("#temp").html(Math.round((data.main.temp * 1.8 - 459.87) * 100) / 100 + "  " + "°F");
        console.log(displayTemp);
        if (data.weather[0].id >= 200 && data.weather[0].id <= 531) {
            $("#main").css("background-image", 'url("img/rain.gif")');
        }
        else if (data.weather[0].id >= 600 && data.weather[0].id <= 622) {
            $("#main").css("background-image", 'url("img/snow.gif")');
        }
        else if (data.weather[0].id >= 701 && data.weather[0].id <= 781) {
            $("#main").css("background-image", 'url("img/fog.gif")');
        }
        else if (data.weather[0].id >= 801 && data.weather[0].id <= 804) {
            $("#main").css({
                "background-image": 'url("img/cloudy.gif")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
        else if (data.weather[0].id >= 900 && data.weather[0].id <= 906) {
            $("#main").css({
                "background-image": 'url("img/extreme.jpg")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
        else if (data.weather[0].id >= 951 && data.weather[0].id <= 962) {
            $("#main").css({
                "background-image": 'url("img/wind.gif")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
        else {
            $("#main").css({
                "background-image": 'url("img/clearsky.gif")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
    }
});
$("#sub").click(function () {
    event.preventDefault();
    var zipcode= $("#zip").val();
    $.ajax({

    url: "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "&appid=1fcda43fd969332cca2ca765913b4481",
    method: 'GET',
    success: function (data) {
        console.log(data);
        console.log($("#location").html(data.name));
        var displayTemp = $("#temp").html(Math.round((data.main.temp * 1.8 - 459.87) * 100) / 100 + "  " + "°F");
        console.log(displayTemp);
        if (data.weather[0].id >= 200 && data.weather[0].id <= 531) {
            $("#main").css("background-image", 'url("img/rain.gif")');
        }
        else if (data.weather[0].id >= 600 && data.weather[0].id <= 622) {
            $("#main").css("background-image", 'url("img/snow.gif")');
        }
        else if (data.weather[0].id >= 701 && data.weather[0].id <= 781) {
            $("#main").css("background-image", 'url("img/fog.gif")');
        }
        else if (data.weather[0].id >= 801 && data.weather[0].id <= 804) {
            $("#main").css({
                "background-image": 'url("img/cloudy.gif")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
        else if (data.weather[0].id >= 900 && data.weather[0].id <= 906) {
            $("#main").css({
                "background-image": 'url("img/extreme.jpg")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
        else if (data.weather[0].id >= 951 && data.weather[0].id <= 962) {
            $("#main").css({
                "background-image": 'url("img/wind.gif")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
        else {
            $("#main").css({
                "background-image": 'url("img/clearsky.gif")',
                "background-repeat": "no-repeat",
                "background-position": "center"
            });
        }
    }
});});

$("#convert").click(function () {
    event.preventDefault();
    var temp = $("#temp").html();
    if (temp.slice(-1)== "F"){
        var c= Math.round((parseFloat(temp) - 32)/ 1.8);
        $("#temp").html(c + "  " + "°C");
        }
 });