document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('profileForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting 

        const formData = new FormData(this);

        fetch("{% url 'profile' %}", {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Handle success 
                window.location.reload(); 
            } else {
                // Show errors
                const errorDiv = document.getElementById('formErrors');
                errorDiv.innerHTML = ''; // Clear previous errors
                for (const [field, errors] of Object.entries(data.errors)) {
                    errors.forEach(error => {
                        errorDiv.innerHTML += `<p>${error}</p>`;
                    });
                }
                errorDiv.style.display = 'block'; // Show error div
            }
        });
    });
});
