function validateForm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    if (email === "" || password === "") {
        errorMessage.style.display = "block";
        errorMessage.innerText = "Both fields are required.";
        return false;
    }

    // Simulate a simple client-side SQL injection check
    //if (email.includes("'") || password.includes("'")) {
    //    errorMessage.style.display = "block";
    //    errorMessage.innerText = "Invalid characters in email or password.";
    //     return false;
    //  }

    return true;
}
