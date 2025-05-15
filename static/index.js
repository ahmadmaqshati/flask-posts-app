
function toggleMenu() {
    const authMenu = document.getElementById("auth-buttons");
    authMenu.classList.toggle("show");
}

function profileClicked() {
    alert("Go to profile");
}

function openLoginModal() {
    alert("Open login modal");
}

function openRegisterModal() {
    alert("Open register modal");
}




function toggleModal() {
    const modal = document.getElementById("modal");
    if (modal.style.display === "flex") {
        modal.style.display = "none";
    } else {
        modal.style.display = "flex";

    }
}


function toggleSignModal() {
    const signupModal = document.getElementById("signupModal");
    if (signupModal.style.display === "flex") {
        signupModal.style.display = "none";
    } else {
        signupModal.style.display = "flex";

    }
}



function openLoginModal() {
    document.getElementById("modal").style.display = "flex";
}





function openRegisterModal() {
    document.getElementById("signupModal").style.display = "flex";

}