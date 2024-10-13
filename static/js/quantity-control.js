document.addEventListener('DOMContentLoaded', function() {
    function handleEnableDisable(itemId) {
        const inputElement = document.querySelector(`.id_qty_${itemId}`);
        let currentValue = parseInt(inputElement.value);
        const stockAmount = parseInt(inputElement.getAttribute('data-stock'));
        const minusButton = document.querySelector(`.decrement-qty_${itemId}`);
        const plusButton = document.querySelector(`.increment-qty_${itemId}`);

        if (isNaN(currentValue) || currentValue < 1) {
            currentValue = 1;
            inputElement.value = currentValue;
        } else if (currentValue > stockAmount) {
            currentValue = stockAmount;
            inputElement.value = currentValue;
        }

        minusButton.disabled = currentValue <= 1;

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
        const stockAmount = parseInt(inputElement.getAttribute('data-stock'));
        let currentValue = parseInt(inputElement.value);

        if (isNaN(currentValue) || currentValue < 1) {
            inputElement.value = 1;
        } else if (currentValue > stockAmount) {
            inputElement.value = stockAmount;
        }
        handleEnableDisable(itemId);
    }

    document.querySelectorAll('.qty_input').forEach(function(inputElement) {
        const itemId = inputElement.getAttribute('data-item_id');
        handleEnableDisable(itemId);
    });

    document.querySelectorAll('.qty_input').forEach(function(inputElement) {
        inputElement.addEventListener('change', function() {
            const itemId = inputElement.getAttribute('data-item_id');
            validateInputValue(itemId);
        });
    });

    document.querySelectorAll('.increment-qty').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();  // Prevent the default form submission
            const itemId = button.getAttribute('data-item_id');
            const inputElement = document.querySelector(`.id_qty_${itemId}`);
            const currentValue = parseInt(inputElement.value);
            const stockAmount = parseInt(inputElement.getAttribute('data-stock'));

            if (currentValue < stockAmount) {
                updateQuantity(itemId, currentValue + 1);
            }
        });
    });

    document.querySelectorAll('.decrement-qty').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault(); 
            const itemId = button.getAttribute('data-item_id');
            const inputElement = document.querySelector(`.id_qty_${itemId}`);
            const currentValue = parseInt(inputElement.value);

            if (currentValue > 1) {
                updateQuantity(itemId, currentValue - 1);
            }
        });
    });
});
