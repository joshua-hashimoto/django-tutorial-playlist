/**
 * Javascript file for controlling bulma.
 */

// modalの開閉用イベントをはる
for (const element of document.querySelectorAll(".modal-close, .show-modal")) {
    const modalId = element.dataset.target;
    const modal = document.getElementById(modalId);
    element.addEventListener("click", (event) => {
        modal.classList.toggle("is-active");
    });
}
