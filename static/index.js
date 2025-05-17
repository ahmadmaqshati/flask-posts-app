console.log(new Date());

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

function handleAddBtnClicked() {
    document.getElementById('addPostModal').style.display = 'flex';
}

function closeAddModal() {
    document.getElementById('addPostModal').style.display = 'none';
}

function submitPost() {
    const username = document.getElementById('post-username').value.trim();
    const title = document.getElementById('title').value.trim();
    const body = document.getElementById('body').value.trim();
    const image = document.getElementById('image').value.trim();
    const userImage = document.getElementById('user_image').value.trim();

    /*  if (username === "" || title === "") {
         alert("Username and Title are required!");
         return;
     } */

    const newPost = {
        username: username,
        title: title,
        body: body,
        image: image,
        user_image: userImage,
        /* date: new Date().toLocaleString(), */
        comments_count: 0
    };

    fetch('/add-post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newPost)
    })
        .then(response => {
            if (response.ok) {
                alert("تمت الإضافة بنجاح!");
                closeAddModal();
                location.reload(); // لإعادة تحميل الصفحة وعرض البوست الجديد
            } else {
                alert("حدث خطأ أثناء الإضافة.");
            }
        });

    console.log("Post to be added:", newPost);
    closeAddModal();
}