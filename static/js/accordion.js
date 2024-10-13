/* global bootstrap */
document.addEventListener('DOMContentLoaded', function() {
    let accordionElements = document.querySelectorAll('.accordion-button');

    accordionElements.forEach(function(button) {
        button.addEventListener('click', function() {
            let target = document.querySelector(this.dataset.mdbTarget);
            let collapse = new bootstrap.Collapse(target);
            collapse.toggle();
        });
    });
});
