document.getElementById('firstname').addEventListener('focus', function (event) {
    document.getElementById("firstname").style.backgroundColor = 'yellow';
});

document.getElementById('firstname').addEventListener('blur', function (event) {
    document.getElementById("firstname").style.backgroundColor = 'white';
});

document.getElementById('lastname').addEventListener('focus', function (event) {
    document.getElementById("lastname").style.backgroundColor = 'yellow';
});

document.getElementById('lastname').addEventListener('blur', function (event) {
    document.getElementById("lastname").style.backgroundColor = 'white';
});

document.getElementById('email').addEventListener('focus', function (event) {
    document.getElementById("email").style.backgroundColor = 'yellow';
});

document.getElementById('email').addEventListener('blur', function (event) {
    document.getElementById("email").style.backgroundColor = 'white';
});

document.getElementById('phone').addEventListener('focus', function (event) {
    document.getElementById('phone').style.backgroundColor = 'yellow';
});

document.getElementById('phone').addEventListener('blur', function (event) {
    document.getElementById('phone').style.backgroundColor = 'white';
});

document.getElementById('comment').addEventListener('focus', function (event) {
    document.getElementById('comment').style.backgroundColor = 'yellow';
});

document.getElementById('comment').addEventListener('blur', function (event) {
    document.getElementById('comment').style.backgroundColor = 'white';
});

document.getElementById('submit').addEventListener("click", function (event) {
    event.preventDefault();
    var firstName = document.getElementById('firstname').value;

    if (firstName.length > 0) {
        document.getElementById('firstNameError').textContent = ""
    }
    else {
        document.getElementById('firstNameError').textContent = "This field cannot be empty.";
        document.getElementById('firstname').style.backgroundColor = 'red';
    }
    var lastName = document.getElementById('lastname').value;
    if (lastName.length > 0) {
        document.getElementById('lastNameError').textContent = ""
    }
    else {
        document.getElementById('lastNameError').textContent = "This field cannot be empty.";
        document.getElementById('lastname').style.backgroundColor = 'red';
    }
    var email = document.getElementById('email').value;
    var regex = /^([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)@([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)[\\.]([a-zA-Z]{2,9})$/;

    if (!regex.test(email)) {
        document.getElementById('emailError').textContent = "Please enter a valid email";
        document.getElementById('email').style.backgroundColor = 'red';
    }
    var phone = document.getElementById("phone").value;
    var reg = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (!reg.test(phone))
        document.getElementById('phoneError').textContent = "Please enter a valid phone number";
    document.getElementById('phone').style.backgroundColor = 'red';


})
;
