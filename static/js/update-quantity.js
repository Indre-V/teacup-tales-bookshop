// Update quantity on click
document.querySelectorAll('.update-link').forEach(function(link) {
    link.addEventListener('click', function(e) {
        var form = this.previousElementSibling; 
        if (form && form.classList.contains('update-form')) {
            form.submit(); // Submit the form
        }
    });
});

// Remove item and reload on click
document.querySelectorAll('.remove-item').forEach(function(link) {
    link.addEventListener('click', function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = this.getAttribute('id').split('remove_')[1];
        var url = `/cart/remove/${itemId}/`;
        var data = new FormData();
        data.append('csrfmiddlewaretoken', csrfToken);

        fetch(url, {
            method: 'POST',
            body: data
        })
        .then(function(response) {
            if (response.ok) {
                location.reload();
            }
        });
    });
});
