document.addEventListener('DOMContentLoaded', function () {

    const addCouponForm = document.getElementById('addCouponForm');
    if (addCouponForm) {
        addCouponForm.addEventListener('submit', function (e) {
            e.preventDefault();
            let formData = new FormData(this);
            let actionUrl = this.getAttribute('action');

            fetch(actionUrl, {
                method: 'POST',
                body: new URLSearchParams(formData), 
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    // Clear previous errors
                    document.querySelectorAll('#addCouponForm .text-danger').forEach(el => el.remove());

                    // Display validation errors
                    for (const [field, errors] of Object.entries(data.errors)) {
                        const inputField = document.querySelector('#addCouponForm [name="' + field + '"]');
                        if (inputField) {
                            let errorDiv = document.createElement('div');
                            errorDiv.classList.add('text-danger');
                            errorDiv.textContent = errors.join(', ');
                            inputField.insertAdjacentElement('afterend', errorDiv);
                        }
                    }
                }
            });
        });
    }

    document.querySelectorAll('.editCouponForm').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            let formData = new FormData(this);
            let actionUrl = this.getAttribute('action');

            fetch(actionUrl, {
                method: 'POST',
                body: new URLSearchParams(formData),
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    location.reload();
                } else {

                    form.querySelectorAll('.text-danger').forEach(el => el.remove());

                    // Display validation errors
                    for (const [field, errors] of Object.entries(data.errors)) {
                        const inputField = form.querySelector('[name="' + field + '"]');
                        if (inputField) {
                            let errorDiv = document.createElement('div');
                            errorDiv.classList.add('text-danger');
                            errorDiv.textContent = errors.join(', ');
                            inputField.insertAdjacentElement('afterend', errorDiv);
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
                body: new URLSearchParams(formData),
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    location.reload();
                }
            });
        });
    });
});
