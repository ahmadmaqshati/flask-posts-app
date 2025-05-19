function submitPost() {
    const username = document.getElementById('post-username').value.trim();
    const title = document.getElementById('title').value.trim();
    const body = document.getElementById('body').value.trim();
    const image = document.getElementById('image').value.trim();
    const userImage = document.getElementById('user_image').value.trim();


    const newPost = {
        username: username,
        title: title,
        body: body,
        image: image,
        user_image: userImage,
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
                alert("Added successfully!");
                closeAddModal();
                location.reload();
            } else {
                alert("An error occurred during the addition.");
            }
        });

    closeAddModal();
}