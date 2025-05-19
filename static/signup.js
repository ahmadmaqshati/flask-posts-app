const signupForm = document.getElementById("signupForm");

// Add an event listener for the form submission
signupForm.addEventListener("submit", function (e) {
    e.preventDefault();

    // Create a FormData object to capture form input values
    const formData = new FormData(signupForm);

    // Construct an object to store user data extracted from the form
    const user = {
        name: formData.get("name"),
        username: formData.get("usernameInput"),
        password: formData.get("passwordInput")
    };

    // Send user data to the server via a POST request
    fetch("/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(user) // Convert user object to JSON format and send it
    })
        .then(res => res.json()) // Parse the JSON response
        .then(data => {
            // Check if the signup was successful
            if (data.status === "success") {
                document.getElementById('email-username').value = '';
                document.getElementById('signup-username').value = '';
                document.getElementById('signup-password').value = '';
                alert("تم التسجيل بنجاح!");
                toggleSignModal();
            } else {
                alert("حدث خطأ أثناء التسجيل");
            }
        })
        .catch(err => {
            alert("فشل في الاتصال بالسيرفر.");
        });
});
