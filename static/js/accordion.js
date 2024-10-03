document.addEventListener('DOMContentLoaded', function() {
    var accordionElements = document.querySelectorAll('.accordion-button');

    accordionElements.forEach(function(button) {
        button.addEventListener('click', function() {
            var target = document.querySelector(this.dataset.mdbTarget);
            var collapse = new bootstrap.Collapse(target);
            collapse.toggle();
        });
    });
});
