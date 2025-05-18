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