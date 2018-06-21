function next() {
    var username = document.getElementById("username").value;

    if (!username) {
        alert("Please enter your user name");
        return;
    }

    var user = localStorage.getItem(username);
    if (!user) {
        alert("User does not exist, please sign up first.");
    }
    else {
        sessionStorage.setItem("user", username);
        window.location.href="EnterPassword.html"
    }
}