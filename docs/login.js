function onStart() {
    onAgreeChecked();
    getLatLong();
}

function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (username == "" || password == "") {
        alert("Please enter your username and password");
        return;
    }

    alert("Under construction")
}

function showpwd() {
    let pwd = document.getElementById("password");
    pwd.type = pwd.type === "password"? "text": "password";
}

function onAgreeChecked() {
    let termsCheckbox = document.getElementById("agree");
    var loginButton = document.querySelector('button[type="submit"]');
    loginButton.disabled = !termsCheckbox.checked;
}

function toUppercase(target) {
    // let uppercase = document.getElementById("uppercase");
    // uppercase.value = uppercase.value.toUpperCase();
    target.value = target.value.toUpperCase();
}

function getLatLong() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            document.getElementById("latitude").value = position.coords.latitude;
            document.getElementById("longitude").value = position.coords.longitude;
        });
    }
}