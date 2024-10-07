document.addEventListener('DOMContentLoaded', function() {
    function handleEnableDisable(itemId) {
        const inputElement = document.querySelector(`.id_qty_${itemId}`);
        let currentValue = parseInt(inputElement.value);
        const stockAmount = parseInt(inputElement.getAttribute('data-stock'));  // Use a custom attribute for stock
        const minusButton = document.querySelector(`.decrement-qty_${itemId}`);
        const plusButton = document.querySelector(`.increment-qty_${itemId}`);

        // Ensure value is not below 1 or exceeds stock amount
        if (isNaN(currentValue) || currentValue < 1) {
            currentValue = 1;
            inputElement.value = currentValue;
        } else if (currentValue > stockAmount) {
            currentValue = stockAmount;
            inputElement.value = currentValue;
        }

        // Enable or disable the decrement button
        minusButton.disabled = currentValue <= 1;

        // Enable or disable the increment button
        plusButton.disabled = currentValue >= stockAmount;
    }

    function updateQuantity(itemId, newQuantity) {
        const inputElement = document.querySelector(`.id_qty_${itemId}`);
        inputElement.value = newQuantity;
        handleEnableDisable(itemId);
    }

    // Validate input value and reset if invalid
    function validateInputValue(itemId) {
        const inputElement = document.querySelector(`.id_qty_${itemId}`);
        const stockAmount = parseInt(inputElement.getAttribute('data-stock'));  // Use custom data attribute
        let currentValue = parseInt(inputElement.value);

        // Ensure the value stays within the allowed range
        if (isNaN(currentValue) || currentValue < 1) {
            inputElement.value = 1;
        } else if (currentValue > stockAmount) {
            inputElement.value = stockAmount;
        }
        handleEnableDisable(itemId);
    }

    // Initial enable/disable check on page load
    document.querySelectorAll('.qty_input').forEach(function(inputElement) {
        const itemId = inputElement.getAttribute('data-item_id');
        handleEnableDisable(itemId);
    });

    // Validate and handle enable/disable every time the input value is manually changed
    document.querySelectorAll('.qty_input').forEach(function(inputElement) {
        inputElement.addEventListener('change', function() {
            const itemId = inputElement.getAttribute('data-item_id');
            validateInputValue(itemId);  // Validate the entered quantity
        });
    });

    // Increment quantity
    document.querySelectorAll('.increment-qty').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();  // Prevent the default form submission
            const itemId = button.getAttribute('data-item_id');
            const inputElement = document.querySelector(`.id_qty_${itemId}`);
            const currentValue = parseInt(inputElement.value);
            const stockAmount = parseInt(inputElement.getAttribute('data-stock'));

            // Increase the quantity if it's less than the stock amount
            if (currentValue < stockAmount) {
                updateQuantity(itemId, currentValue + 1);
            }
        });
    });

    // Decrement quantity
    document.querySelectorAll('.decrement-qty').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();  // Prevent the default form submission
            const itemId = button.getAttribute('data-item_id');
            const inputElement = document.querySelector(`.id_qty_${itemId}`);
            const currentValue = parseInt(inputElement.value);

            // Decrease the quantity if it's greater than 1
            if (currentValue > 1) {
                updateQuantity(itemId, currentValue - 1);
            }
        });
    });
});
