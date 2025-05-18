/* function openModal() {
    document.getElementById("delete-post-modal").style.display = "flex";

} */

function closeModal() {
    setTimeout(() => {
        document.getElementById("delete-post-modal").style.display = "none";
    }, 100);
}




function openModal(postId, postTitle) {
    document.getElementById('delete-post-id-input').value = postId;
    document.getElementById('delete-post-title').innerText = postTitle;
    document.getElementById('delete-post-modal').style.display = 'flex';
}

/* function closeModal() {
    document.getElementById('delete-post-modal').style.display = 'none';
} */







function confirmPostDelete() {
    const postId = document.getElementById('delete-post-id-input').value;

    fetch(`/delete-post/${postId}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (response.ok) {
                closeModal();
                // حذف العنصر من DOM مباشرةً
                document.getElementById(`post-${postId}`).remove();
            } else {
                alert("Failed to delete post.");
            }
        })
        .catch(error => {
            console.error("Error deleting post:", error);
        });
}