'use strict';

let menuEl = document.querySelectorAll('.menu_block');
menuEl.forEach(element => {
    element.classList.add('menu_block');
    element.addEventListener('click', () => {
        element.classList.remove('menu_block');
    });
});