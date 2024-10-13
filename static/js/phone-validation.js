document.addEventListener('DOMContentLoaded', function () {

    const checkoutForm = document.getElementById('checkout-form');
    const phoneNumberInput = document.querySelector('input[name="phone_number"]');
    
    function validatePhoneNumber() {
        const phoneNumber = phoneNumberInput.value.trim();
        const phoneNumberPattern = /^\+\d{7,15}$/; 
        
        if (phoneNumber === '') {
            showValidationError(phoneNumberInput, 'Phone number cannot be empty.');
            return false;
        } else if (!phoneNumber.match(phoneNumberPattern)) {
            showValidationError(phoneNumberInput, 'Phone number must start with "+" and contain only digits (7 to 15 digits).');
            return false;
        } else {
            clearValidationError(phoneNumberInput);
            return true;
        }
    }

    function showValidationError(input, message) {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
        input.setCustomValidity(message);
    }

    function clearValidationError(input) {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
        input.setCustomValidity('');
    }

    phoneNumberInput.addEventListener('input', validatePhoneNumber);
    phoneNumberInput.addEventListener('blur', validatePhoneNumber);

});