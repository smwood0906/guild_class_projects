/**
 This project is to recreate the AngryDice Game that I originally created in Python. Completed during Week 8 of Bootcamp.
 */
$("#phase").html(" 1");
var phase = 1;
var die1 = new Dice();
var die2 = new Dice();

/* click event for hold button*/

$("#hold1").click(function(){
    if(die2.held==true){
        alert("Sorry, you cannot hold both dice.")
    }
    else{
    die1.hold(die2.held, 'dice1')}}
);
$("#hold2").click(function() {
    if (die1.held == true) {
        alert("Sorry you cannot hold both dice.")
    }
    else {
        die2.hold(die1.held, 'dice2')
    }
});

/*create Dice object*/
function Dice() {
    this.value = 0;
    this.held = false;
/* roll method to receive a random value for a 6 sided dice*/
    this.roll = function () {
        if (!this.held) {
            this.value = Math.floor(Math.random() * 6) + 1;
        }

    };
/* method to display dice image*/
    this.render = function (locationID) {
        var loc = document.getElementById(locationID);
        if (this.value == "3") {
            loc.innerHTML+='<img id="' + "3" + '" src="3.png">';
        }

        else {
            loc.innerHTML+="<img src='" + this.value + ".png'>"
        }
    };
/* method to hold the value of one dice*/
    this.hold = function(heldValue, divID ){
        if(!heldValue){
            if(this.value==6){
                alert("Sorry, you cannot hold a 6.")
            }
            else if(this.held==false){
                this.held = true;
                $("#" + divID).addClass('border');
            }
            else{
                this.held = false;
                $("#" + divID).removeClass('border');
            }
        }

    }
}
/* click event to run roll and render methods and check phase*/
$("#roll").click(function () {
    $("#dice1").html("");
    $("#dice2").html("");
    die1.roll();
    die2.roll();
    die1.render('dice1');
    die2.render('dice2');
    checkPhase();
});

/*check phase of game and change phase HTML*/
function checkPhase(){
    if(die1.value==3 && die2.value==3){
        $("#message").html("ANGRY DICE! You must go back to Phase 1!");
        $("#phase").html(" 1");
        die1.held=false;
        die2.held=false;
        phase = 1;
    }
    else if(phase==1 && die1.value + die2.value === 3){
        $("#phase").html(" 2");
        phase = 2;
        die1.held=false;
        die2.held=false;
    }
    else if(phase==2 && (die1.value==3 && die2.value==4 || die1.value==4 && die2.value==3 )){
        $("#phase").html(" 3");
        phase = 3;
        die1.held=false;
        die2.held=false;
    }
    else if(phase==3 && (die1.value==5 && die2.value==6 || die1.value==6 && die2.value==5)){
        $("#phaseContainer").html("YOU WIN!");
        die1.held=false;
        die2.held=false;
    }

}
/* create multiple players*/
// var Pl_lst = [];
// function Players() {
//     this.name = $("#players").val();
// }
// $("#sub").click(function () {
//     event.preventDefault();
//     if (Pl_lst.length < 1) {
//         player1 = new Players();
//         Pl_lst.push(player1);
//         $("#players").val("");
//         $("#players").attr("placeholder", "Player 2 Name")
//     }
//     else {
//         player2 = new Players();
//         Pl_lst.push(player2);
//         console.log(Pl_lst);
//         // $("#nameInput").css("display", "none");
//         $("#nameInput").hide();
//         $("#turn").html((Pl_lst[0].name) + "  it's your turn!");
//     }
// });



