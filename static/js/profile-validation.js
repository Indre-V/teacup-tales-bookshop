document.addEventListener('DOMContentLoaded', function() {
    // Handle profile form submission
    const profileForm = document.getElementById('profileForm');
    if (profileForm) {
        profileForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const url = profileForm.getAttribute('data-url'); // Get the URL from the data-url attribute

            fetch(url, {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                handleResponse(data, profileForm);
            });
        });
    }

    // Handle user form submission
    const userForm = document.getElementById('userForm');
    if (userForm) {
        userForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const url = userForm.getAttribute('data-url'); // Get the URL from the data-url attribute

            fetch(url, {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                handleResponse(data, userForm);
            });
        });
    }

    // Function to handle form response
    function handleResponse(data, form) {
        // Clear all previous errors
        form.querySelectorAll('.error-message').forEach(errorElement => {
            errorElement.remove(); // Remove previous error messages
        });

        if (data.success) {
            window.location.reload(); // Reload on success
        } else {
            // Loop through the errors and display them under each corresponding form field
            for (const field in data.errors) {
                if (data.errors.hasOwnProperty(field)) {
                    const inputElement = form.querySelector(`[name="${field}"]`);
                    if (inputElement) {
                        // Create the error message element
                        data.errors[field].forEach(error => {
                            const errorElement = document.createElement('p');
                            errorElement.textContent = error;
                            errorElement.classList.add('text-danger', 'error-message'); // Style the error message
                            inputElement.after(errorElement); // Insert the error message right after the input field
                        });
                    }
                }
            }
        }
    }
});
