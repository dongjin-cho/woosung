document.addEventListener('DOMContentLoaded', () => {
    const burger = document.getElementById('burger-menu');
    const nav = document.querySelector('.nav');

    if (burger && nav) {
        burger.addEventListener('click', () => {
            nav.classList.toggle('active');
            burger.classList.toggle('toggle');
        });
    }
});
