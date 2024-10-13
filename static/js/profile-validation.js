document.addEventListener('DOMContentLoaded', function() {
    const profileForm = document.getElementById('profileForm');
    if (profileForm) {
        profileForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const url = profileForm.getAttribute('data-url');

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

    const userForm = document.getElementById('userForm');
    if (userForm) {
        userForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const url = userForm.getAttribute('data-url');

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

    function handleResponse(data, form) {

        form.querySelectorAll('.error-message').forEach(errorElement => {
            errorElement.remove();
        });

        if (data.success) {
            window.location.reload();
        } else {

            for (const field in data.errors) {
                if (data.errors.hasOwnProperty(field)) {
                    const inputElement = form.querySelector(`[name="${field}"]`);
                    if (inputElement) {

                        data.errors[field].forEach(error => {
                            const errorElement = document.createElement('p');
                            errorElement.textContent = error;
                            errorElement.classList.add('text-danger', 'error-message'); 
                            inputElement.after(errorElement);
                        });
                    }
                }
            }
        }
    }
});
