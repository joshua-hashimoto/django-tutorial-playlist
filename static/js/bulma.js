/**
 * Javascript file for controlling bulma.
 */

// modalの開閉用イベントをはる
for (const element of document.querySelectorAll(
    ".modal .delete, .show-modal"
)) {
    element.addEventListener("click", (event) => {
        const modalId = element.dataset.target;
        const modal = document.getElementById(modalId);
        modal.classList.toggle("is-active");
    });
}
