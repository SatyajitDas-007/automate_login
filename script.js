// script.js

function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Check if the username and password match a predefined value (for demonstration purposes)
    if (username === "Satyajit" && password === "satya1") {
        document.getElementById("result").textContent = "Login Successful";
    } else {
        document.getElementById("result").textContent = "Login Failed. Please check your username and password.";
    }
}
