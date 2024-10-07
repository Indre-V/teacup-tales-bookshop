document.addEventListener('DOMContentLoaded', function () {
    // Get references to the elements
    const filterElement = document.getElementById('advancedFilterCollapse');
    const buttonElement = document.getElementById('toggleButton');

    // Function to toggle the collapse based on screen width
    function toggleFilter() {
        const screenWidth = window.innerWidth;

        if (screenWidth >= 768) {
            // Remove collapse behavior and ensure the filter is expanded
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

    // Initial check when the page loads
    toggleFilter();

    // Re-check on window resize
    window.addEventListener('resize', toggleFilter);
});
