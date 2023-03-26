const threebars = document.querySelector('.three-bars');
const mobile_menu = document.querySelector('.mobile-nav');

threebars.addEventListener('click', function () {
    this.classList.toggle('is-active');
    mobile_menu.classList.toggle('is-active');
});