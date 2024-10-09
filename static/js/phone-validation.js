document.addEventListener('DOMContentLoaded', function () {
    // Get the form and the phone number input field
    const checkoutForm = document.getElementById('checkout-form');
    const phoneNumberInput = document.querySelector('input[name="phone_number"]');
    
    // Function to validate phone number
    function validatePhoneNumber() {
        const phoneNumber = phoneNumberInput.value.trim();
        const phoneNumberPattern = /^\+\d{7,15}$/;  // Only + and digits, 7 to 15 digits after '+'
        
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

    // Show validation error
    function showValidationError(input, message) {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
        input.setCustomValidity(message);
    }

    // Clear validation error
    function clearValidationError(input) {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
        input.setCustomValidity('');
    }

    // Validate phone number in real-time when typing or when the input loses focus
    phoneNumberInput.addEventListener('input', validatePhoneNumber);
    phoneNumberInput.addEventListener('blur', validatePhoneNumber);

});