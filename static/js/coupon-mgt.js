document.addEventListener('DOMContentLoaded', function () {
    
    // Handle Add Coupon Form Submission
    document.querySelector('#addCouponForm').addEventListener('submit', function (e) {
        e.preventDefault();
        let formData = new FormData(this);
        let actionUrl = this.getAttribute('action');
        
        fetch(actionUrl, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();  // Reload the page to show the updated list
            } else {
                // Clear previous errors
                this.querySelectorAll('.text-danger').forEach(el => el.remove());
                
                // Display validation errors
                for (const [field, errors] of Object.entries(data.errors)) {
                    let input = this.querySelector(`[name="${field}"]`);
                    if (input) {
                        let errorDiv = document.createElement('div');
                        errorDiv.classList.add('text-danger');
                        errorDiv.textContent = errors.join(', ');
                        input.after(errorDiv);
                    }
                }
            }
        });
    });

    // Handle Edit Coupon Form Submission for each edit form
    document.querySelectorAll('.editCouponForm').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            let formData = new FormData(this);
            let actionUrl = this.getAttribute('action');
            
            fetch(actionUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    // Clear previous errors
                    this.querySelectorAll('.text-danger').forEach(el => el.remove());

                    // Display validation errors
                    for (const [field, errors] of Object.entries(data.errors)) {
                        let input = this.querySelector(`[name="${field}"]`);
                        if (input) {
                            let errorDiv = document.createElement('div');
                            errorDiv.classList.add('text-danger');
                            errorDiv.textContent = errors.join(', ');
                            input.after(errorDiv);
                        }
                    }
                }
            });
        });
    });

    // Handle Delete Coupon Form Submission
    document.querySelectorAll('.deleteCouponForm').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            let formData = new FormData(this);
            let actionUrl = this.getAttribute('action');
            
            fetch(actionUrl, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();  // Reload the page to show the updated list
                }
            });
        });
    });
});
