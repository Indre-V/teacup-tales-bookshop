document.querySelectorAll('.update-link').forEach(function(link) {
    link.addEventListener('click', function(e) {
        let form = this.previousElementSibling; 
        if (form && form.classList.contains('update-form')) {
            form.submit(); 
        }
    });
});

document.querySelectorAll('.remove-item').forEach(function(link) {
    link.addEventListener('click', function(e) {
        let csrfToken = "{{ csrf_token }}";
        let itemId = this.getAttribute('id').split('remove_')[1];
        let url = `/cart/remove/${itemId}/`;
        let data = new FormData();
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
