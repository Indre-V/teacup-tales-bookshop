document.addEventListener('DOMContentLoaded', function() {
    // Function to check window width and toggle collapse behavior
    function toggleFilter() {
        let filterElement = document.getElementById('advancedFilterCollapse');
        let buttonElement = document.getElementById('toggleButton');

        if (window.innerWidth >= 768) { 
            // Disable collapse functionality for screens 820px and above
            filterElement.classList.add('show'); // Ensure it is shown
            filterElement.classList.remove('collapse'); // Remove collapse behavior
            filterElement.style.height = 'auto'; // Set height explicitly to auto to prevent collapsing
            buttonElement.removeAttribute('data-bs-toggle'); // Disable collapse toggle on button
        } else {
            // Enable collapse functionality for smaller screens
            filterElement.classList.add('collapse'); // Enable collapse
            filterElement.classList.remove('show'); // Ensure it starts collapsed
            buttonElement.setAttribute('data-bs-toggle', 'collapse'); // Re-enable collapse on button
        }
    }

    // Run on page load
    toggleFilter();

    // Run on window resize
    window.addEventListener('resize', function() {
        toggleFilter();
    });
});