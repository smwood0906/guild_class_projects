$('input[type=text]').focus(function () {
    $(this).css("backgroundColor", "yellow");
});

$('input[type=text]').blur(function () {
    $(this).css("backgroundColor", "white");
});

$('#submit').click(function () {
    event.preventDefault();

    var firstname = $("#firstname").val()
    var lastname = $("#lastname").val()

    if (firstname > 0) {
        $("#firstname").html("");
    } else {
        $("#firstNameError").html("This field cannot be blank.").css("color", "red");

        if (lastname > 0) {
            $("#lastname").html("");
        } else {
            $("#lastNameError").html("This field cannot be blank.").css("color", "red");
        }
    }

});

$('#email').keyup(function () {
    var email = $('#email').val();
    var regex = /^([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)@([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)[\\.]([a-zA-Z]{2,9})$/;

    if (!regex.test(email)) {
        $('#emailError').html("Please enter a valid email address.");
        $('#errIcon').html('<i style="color:red" class="glyphicon glyphicon-remove"></i>');
    } else {
        $('#emailError').html("");
        $('#errIcon').html('<i style="color:green" class="glyphicon glyphicon-ok"></i>');
    }
});

$('#phone').keyup(function () {
    var phone = $("#phone").val();
    var reg = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!reg.test(phone)) {
        $('#phoneError').html("Please enter a valid phone number");
        $('#errIcon2').html('<i style="color:red" class="glyphicon glyphicon-remove"></i>');
    }
    else {
        $('#phoneError').html("");
        $('#errIcon2').html('<i style="color:green" class="glyphicon glyphicon-ok"></i>');
    }
})
;


