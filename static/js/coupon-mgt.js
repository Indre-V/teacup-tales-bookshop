 $(document).ready(function () {
    // Handle Add Coupon Form Submission
    $('#addCouponForm').submit(function (e) {
        e.preventDefault();
        let formData = $(this).serialize(); 
        $.post($(this).attr('action'), formData, function (data) {
            if (data.success) {
                location.reload();  // Reload the page to show the updated list
            } else {
                // Clear previous errors
                $('#addCouponForm .text-danger').remove();
                // Display validation errors
                for (const [field, errors] of Object.entries(data.errors)) {
                    $('#addCouponForm [name="' + field + '"]').after('<div class="text-danger">' + errors.join(', ') + '</div>');
                }
            }
        });
    });

    // Handle Edit Coupon Form Submission for each edit form
    $('.editCouponForm').submit(function (e) {
        e.preventDefault();
        let formData = $(this).serialize();
        let $form = $(this);  
        $.post($form.attr('action'), formData, function (data) {
            if (data.success) {
                location.reload();  
            } else {

                $('.editCouponForm .text-danger').remove();
                // Display validation errors
                for (const [field, errors] of Object.entries(data.errors)) {
                    $('.editCouponForm [name="' + field + '"]').after('<div class="text-danger">' + errors.join(', ') + '</div>');
                }
            }
        });
    });

    // Handle Delete Coupon Form Submission
    $('.deleteCouponForm').submit(function (e) {
        e.preventDefault();
        let formData = $(this).serialize(); // Using let instead of var
        $.post($(this).attr('action'), formData, function (data) {
            if (data.success) {
                location.reload();  // Reload the page to show the updated list
            }
        });
    });
});
