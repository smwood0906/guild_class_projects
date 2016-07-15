/**
 * Created by adamtwood on 7/12/2016.
 */
var Pl_lst = [];
var die1 = new Dice();
var die2 = new Dice();

function Players() {
    this.name = $("#players").val();
}

function Dice() {
    this.value = 0;
    this.held = false;

    this.roll = function () {
        if (!this.held) {
            this.value = Math.floor(Math.random() * 6) + 1;

        }
    };

    this.render = function (locationID) {
        var loc = document.getElementById(locationID);
        if (this.value == "3") {
            loc.innerHTML+='<img id="' + "3" + '" src="3.png">';
        }


        else {
            loc.innerHTML+="<img src='" + this.value + ".png'>"
        }
    }
}


$("#roll").click(function () {
    $("#dice1").html("");
    $("#dice2").html("");
    die1.roll();
    die2.roll();
    die1.render('dice1');
    die2.render('dice2');
});

$("#sub").click(function () {
    event.preventDefault();
    if (Pl_lst.length < 1) {
        player1 = new Players();
        Pl_lst.push(player1);
        $("#players").val("");
        $("#players").attr("placeholder", "Player 2 Name")
    }
    else {
        player2 = new Players();
        Pl_lst.push(player2);
        console.log(Pl_lst);
        // $("#nameInput").css("display", "none");
        $("#nameInput").hide();
        $("#turn").html((Pl_lst[0].name) + "  it's your turn!");
    }
});



