document.addEventListener('DOMContentLoaded', function () {

    const filterElement = document.getElementById('advancedFilterCollapse');
    const buttonElement = document.getElementById('toggleButton');

    function toggleFilter() {
        const screenWidth = window.innerWidth;

        if (screenWidth >= 768) {

            filterElement.classList.add('show');
            filterElement.classList.remove('collapse');
            filterElement.style.height = 'auto'; 
            buttonElement.removeAttribute('data-bs-toggle');
        } else {
            // Add collapse behavior for screens smaller than 768px
            filterElement.classList.add('collapse');
            filterElement.classList.remove('show');
            buttonElement.setAttribute('data-bs-toggle', 'collapse');
        }
    }

    toggleFilter();

    window.addEventListener('resize', toggleFilter);
});
