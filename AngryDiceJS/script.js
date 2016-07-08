$("#sub").click(function () {
    event.preventDefault();
    var num = parseInt($("#number").val());
    var lst = "";
    for (var i = 1; i <= num; i++) {
        lst += "<img src='" + (Math.floor(Math.random() * 6) + 1) + ".png'>"
    }
    $("#dice").html(lst);

});

