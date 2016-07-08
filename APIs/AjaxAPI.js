$("#sub").click(function () {
    event.preventDefault();
$.ajax({
    url: "http://ron-swanson-quotes.herokuapp.com/v2/quotes",
    method: "GET",
    success: function (data) {
        console.log(data);
        console.log($("#quote").html(data))
    }
})});