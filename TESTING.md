 # Testing

Return back to the [README.md](README.md) file.

![Main Image](/docs/readme-md/main-image.png)

# Contents

- [Responsiveness Tests](#responsiveness-tests)
- [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Python (Unit Testing)](#python--unit-testing-)
- [Manual Testing](#manual-testing)
- [Role-based Restrictions](#role-based-restrictions)
- [Bugs](#bugs)
- [Browser Compatibility](#browser-compatibility)
- [User Story Testing](#user-story-testing)
- [Lighthouse Testing](#lighthouse-testing)
- [Accessibility Testing](#accessibility-testing)




## Responsiveness Tests

I followed the mobile-first strategy and verified all of my modifications using the DevTools browsers for Google Chrome and Microsoft Edge. Deployed versions were tested using the external website [Responsive Design Checker](https://responsivedesignchecker.com/ "Responsive Design Checker"). The [Am I Responsive](https://ui.dev/amiresponsive "Am I responsive") website was another external source that was used to obtain a unified view of different device breakpoints.

I have also used Google Chrome's Mobile Simulator extension to evaluate the responsiveness of even more specialized devices. Device samples were examined for navigation, element alignment, content layout, and functionality concerns at different breakpoints.

Final Test Results:

| Size | Device Example     | Navigation | Element Alignments | Content Placement | Functionality | Notes                             |
| ---- | ------------------ | ---------- | ------------------ | ----------------- | ------------- | --------------------------------- |
| sm   | Samsung Galaxy S20 | &check;    | &check;            | &check;           | &check;       |                                   |
| sm   | iPhone 11 PRO      | &check;    | &check;            | &check;           | &check;       |
| sm   | iPhone 13 PRO MAX  | &check;    | &check;            | &check;           | &check;       |
| md   | iPad MINI          | &check;    | &check;            | &check;           | &check;       |                                   |
| md   | Galaxy Tab S7      | &check;    | &check;            | &check;           | &check;       |                                   |
| md   | iPad Air           | &check;    | &check;            | &check;           | &check;       |                                   |
| lg   | iPad Pro           | &check;    | &check;            | &check;           | &check;       |  |
| xl   | Mackbook Air       | &check;    | &check;            | &check;           | &check;       |                                   |
| xl   | HP Stream Laptop   | &check;    | &check;            | &check;           | &check;       |                                   |
| xxl  | Dell Lattitude     | &check;    | &check;            | &check;           | &check;       |                                   |
| xxl  | Desktop            | &check;    | &check;            | &check;           | &check;       |                                   |

[Back to top](#contents)


## Code Validation

### HTML

The recommended [HTML W3C Validator](https://validator.w3.org) to validate all of the project's HTML files.

This is the process which was followed of validating an HTML file by direct input:

1. **Access the Validator**: Visit the [W3C Markup Validation Service](https://validator.w3.org/).
2. **Choose Direct Input**: Select the "Validate by Direct Input" tab.
3. **Paste Your HTML Code**: Copy HTML code and paste it into the text box.
4. **Validate**: Click the "Check" button to validate HTML.

<details>

<summary>HTML Validation Results</summary>

</details>


[Back to top](#contents)

### CSS

The [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) tool, provided by the W3C, enables to validate and verify the correctness of CSS code. It ensures that your web pages adhere to W3C standards, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|CSS file | No errors |<details><summary>Result Summary</summary>![Result](docs/testing-md/validations/css-test.png)</details>| ✅


### JavaScript

### Python

The python files have all been passed through [PEP8 CI Online](https://pep8ci.herokuapp.com/)

<details><summary><b>PEP8 Test Results</b></summary>

</details><br/>

[Back to top](#contents)



### Python (Unit Testing)

Python's `unittest` framework offers a robust and flexible testing solution. 
Ideally, every part of the project should be put through the robust automated testing. Due to time constraints I have conentrated automated tests concentrated on CRUD related functionality views, models and forms. 

The automated tests highlighted a redundant view and html file naming issue. Although these issues did not affect the functionality of the application, the quality and maintainability of the code are equally important. 

![Unittest](/docs/testing-md/automated-test-results.png)



[Back to top](#contents)

## Manual Testing

In addition to using `unittest`, extensive manual testing was performed on the application. Each feature was verified against success criteria. Where applicable, negative testing was conducted by providing invalid or unexpected inputs to assess the application's robustness in handling errors and exceptions.

<details><summary><b>Manual Testing Results</b></summary>


**AUTHENTICATION**

| Test Case                            | Element                                            | Action                                                                                 | Expected Outcome                                                                                                                                                                                       | Result |
| ------------------------------------ | -------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| Register with Valid Credentials      | Registration form fields (email address, password) | Fill out the form with valid credentials and submit.                                   | User is redirected to the home page after successful registration and iemail verification message displayed.                                                                                           | ✅      |
| Register with Existing email address | Registration form fields (email address, password) | Attempt to register with a email address that already exists.                          | Registration fails with appropriate error message ("email address already exists"). User remains on the registration page.                                                                             | ✅      |
| Register with Blank Fields           | Registration form fields (email address, password) | Leave one or both required fields (email address, password) blank and submit the form. | Registration fails with appropriate error messages for each blank field. User remains on the registration page.                                                                                        | ✅      |
| Login with Valid Credentials         | Login form fields (email address, password)        | Fill out the form with valid email address and password and submit.                    | User is redirected to the home page after successful login. Success message displayed with email address.                                                                                              | ✅      |
| Login with Invalid email address     | Login form fields (email address, password)        | Attempt to login with an invalid email address.                                        | Login fails with appropriate error message ("Please enter a correct email address and password"). User remains on the login page.                                                                      | ✅      |
| Login with Incorrect Password        | Login form fields (email address, password)        | Attempt to login with a valid email address but incorrect password.                    | Login fails with appropriate error message ("Please enter a correct email address and password"). User remains on the login page.                                                                      | ✅      |
| Login with Blank Fields              | Login form fields (email address, password)        | Leave email address or password field blank and submit the form.                       | Login fails with appropriate error messages for each blank field. User remains on the login page.                                                                                                      | ✅      |
| Logout                               | Logout link or button                              | Click on the logout link/button while authenticated.                                   | User is logged out and redirected to the home page. Navigation bar updates to reflect non-authenticated state (e.g., "Login" and "Register" links). Log out notification displayed with email address. | ✅      |

**REVIEWS**

| Test Case                          | Element                  | Action                         | Expected Outcome                                                                                          | Result |
| ---------------------------------- | ------------------------ | ------------------------------ | --------------------------------------------------------------------------------------------------------- | ------ |
| Display reviews                    | Reviews container        | View existing reviews          | All reviews associated with the post are displayed, showing author's email address and creation time.     | ✅      |
| Display Review Timestamp           | Review timestamp         | View review creation time      | Review creation time is displayed in a human-readable format (e.g., "2 days ago").                        | ✅      |
| Edit review (Owner or Superuser)   | Edit button              | Click on edit button           | Redirects to edit review page if user is review owner or superuser.                                       | ✅      |
| Delete review (Owner or Superuser) | Delete button            | Click on delete button         | Shows delete confirmation modal and deletes review if user confirms action.                               | ✅      |
| No reviews Available               | "No reviews yet" message | No reviews exist for the post  | Message "No reviews yet." is displayed.                                                                   | ✅      |
| Submit review                      | Review form              | Enter review and submit        | review is successfully added and displayed in the reviews section.                                        | ✅      |
| Authenticate review Submission     | "Posting as" message     | User is authenticated          | Shows message "Posting as: username" above the review form.                                               | ✅      |
| Display Login Prompt               | "Log in" link            | User is not authenticated      | Shows link "Log in to leave a review" prompting user to log in.                                           | ✅      |
| Form Validation Error              | Submit button            | Submit empty or invalid review | Displays error messages next to form fields, prompting user to correct them.                              | ✅      |
| Buyer reviews                      | Review Container         | Add Review                     | Container not available if the product has not been purchased by the user unless the user is a superuser. | ✅      |

**ALL BOOKS**

| Test Case                                  | Element                        | Action                                                            | Expected Outcome                                               | Result |
| ------------------------------------------ | ------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------- | ------ |
| Toggle Advanced Search                     | ToggleButton (Advanced Filter) | Click the toggle button                                           | Advanced search options should expand/collapse                 | ✅      |
| Search by Author                           | Author Input Field             | Enter author name and submit                                      | Search results should be filtered by the specified author      | ✅      |
| Search by Title                            | Title Input Field              | Enter title and submit                                            | Search results should be filtered by the specified title       | ✅      |
| Search by Description                      | Description Input Field        | Enter description and submit                                      | Search results should be filtered by the specified description | ✅      |
| Search by ISBN                             | ISBN Input Field               | Enter ISBN and submit                                             | Search results should be filtered by the specified ISBN        | ✅      |
| Filter by Genre                            | Genre Checkbox                 | Select one or more genres                                         | Search results should be filtered by selected genres           | ✅      |
| Filter by Category                         | Category Checkbox              | Select one or more categories                                     | Search results should be filtered by selected categories       | ✅      |
| Filter by Price Range                      | Price Range Checkbox           | Select a price range                                              | Search results should be filtered by selected price range      | ✅      |
| Reset Filters                              | Reset Button                   | Click the reset button                                            | All filters should be cleared                                  | ✅      |
| Sort by Title (A to Z)                     | Sort Dropdown                  | Select 'Title (A to Z)' and submit                                | Results should be sorted by Title in ascending order           | ✅      |
| Sort by Title (Z to A)                     | Sort Dropdown                  | Select 'Title (Z to A)' and submit                                | Results should be sorted by Title in descending order          | ✅      |
| Add Product to Wishlist                    | Wishlist Button                | Click on the wishlist button                                      | The product should be added to the user's wishlist             | ✅      |
| Add Product to Cart                        | Add to Cart Button             | Click on the 'Add to Cart' button                                 | The product should be added to the shopping cart               | ✅      |
| Search by Author (Failure Expected)        | Author Input Field             | Enter special characters or numbers in the author name field      | Search results are not filtered by the specified author        | ✅      |
| Search by Title (Failure Expected)         | Title Input Field              | Enter a very long string or special characters in the title field | Search results are not filtered by the specified title         | ✅      |
| Search by Description (Failure Expected)   | Description Input Field        | Enter invalid HTML or script tags in the description field        | Search results are not filtered by the specified description   | ✅      |
| Search by ISBN (Failure Expected)          | ISBN Input Field               | Enter non-numeric values in the ISBN field                        | Search results are not filtered by the specified ISBN          | ✅      |
| Filter by Genre (Failure Expected)         | Genre Checkbox                 | Select multiple conflicting genres, or uncheck all genres         | Search results are not filtered by selected genres             | ✅      |
| Filter by Category (Failure Expected)      | Category Checkbox              | Select multiple conflicting categories, or uncheck all categories | Search results are not filtered by selected categories         | ✅      |
| Filter by Price Range (Failure Expected)   | Price Range Checkbox           | Enter negative values or invalid price ranges                     | Search results are not filtered by selected price range        | ✅      |
| Reset Filters (Failure Expected)           | Reset Button                   | Click reset after entering invalid inputs in the search fields    | Filters are not cleared after clicking reset                   | ✅      |
| Sort by Title (A to Z) (Failure Expected)  | Sort Dropdown                  | Select an invalid or non-existent sorting option from dropdown    | Results are not sorted by Title in ascending order             | ✅      |
| Sort by Title (Z to A) (Failure Expected)  | Sort Dropdown                  | Select an invalid or non-existent sorting option from dropdown    | Results are not sorted by Title in descending order            | ✅      |
| Add Product to Wishlist (Failure Expected) | Wishlist Button                | Try to add the same product multiple times rapidly to wishlist    | The product is not added to the user's wishlist                | ✅      |
| Add Product to Cart (Failure Expected)     | Add to Cart Button             | Try to add an out-of-stock product to the cart                    | The add to cart icon is not displayed                          | ✅      |

**SPECIAL OFFERS**

| Test Case                                        | Element               | Action                                                    | Expected Outcome                                                                                     | Result |
| ------------------------------------------------ | --------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------ |
| Toggle Sort Options                              | Sort Dropdown         | Click on the Sort dropdown                                | The dropdown should display sorting options (Title A-Z, Title Z-A, Price Low-High, Price High-Low)   | ✅      |
| Sort by Title (A to Z)                           | Sort Dropdown         | Select 'Title (A to Z)' and submit                        | Products should be sorted by Title in ascending alphabetical order                                   | ✅      |
| Sort by Title (Z to A)                           | Sort Dropdown         | Select 'Title (Z to A)' and submit                        | Products should be sorted by Title in descending alphabetical order                                  | ✅      |
| Sort by Price (Low to High)                      | Sort Dropdown         | Select 'Price (Low to High)' and submit                   | Products should be sorted by Price from lowest to highest                                            | ✅      |
| Sort by Price (High to Low)                      | Sort Dropdown         | Select 'Price (High to Low)' and submit                   | Products should be sorted by Price from highest to lowest                                            | ✅      |
| Add Product to Wishlist                          | Wishlist Button       | Click on the wishlist button                              | Product should be added to the user’s wishlist, and a confirmation message should be displayed       | ✅      |
| Add Product to Cart                              | Add to Cart Button    | Click on the 'Add to Cart' button                         | Product should be added to the shopping cart, and the cart should update with the new item           | ✅      |
| Display Sale Tag                                 | Product Image/Tags    | View product with a sale tag                              | Sale tag should be displayed if the product is on sale                                               | ✅      |
| Verify Price Reduction (Sale)                    | Product Price Display | View product prices with sales                            | Sale price should be less than the regular price, and the original price should have a strikethrough | ✅      |
| Navigate to Product Details                      | Product Image         | Click on the product image                                | The user should be redirected to the product details page                                            | ✅      |
| Verify Pagination (Next)                         | Pagination Controls   | Click 'Next' on pagination                                | The user should be navigated to the next page of products                                            | ✅      |
| Verify Pagination (Last)                         | Pagination Controls   | Click 'Last' on pagination                                | The user should be navigated to the last page of product listings                                    | ✅      |
| Sort Dropdown Invalid Option (Failure)           | Sort Dropdown         | Enter an invalid sorting option (e.g., random string)     | Sorting should fail, and an error message should be displayed                                        | ✅      |
| Add Out of Stock Product to Cart (Failure)       | Add to Cart Button    | Try adding a product marked as 'Out of Stock' to the cart | Adding to the cart should fail, and an error message should be displayed                             | ✅      |
| Add Product Multiple Times to Wishlist (Failure) | Wishlist Button       | Rapidly click to add the same product to the wishlist     | Only one instance of the product should be added, and repeated attempts should display an error      | ✅      |


**CART**

| Test Case                                     | Element                 | Action                                                            | Expected Outcome                                                             | Result |
| --------------------------------------------- | ----------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------ |
| Display Product in Cart                       | Product Image and Title | View the product image and title in the cart                      | Product details (image, title, author) should display correctly in the cart  | ✅      |
| Update Quantity                               | Quantity Selector       | Change the quantity value and submit                              | The quantity should update and reflect in the total price                    | ✅      |
| Decrease Quantity                             | Decrement Button        | Click the decrement button to reduce quantity                     | The quantity should decrease and update the total price                      | ✅      |
| Increase Quantity                             | Increment Button        | Click the increment button to increase quantity                   | The quantity should increase and update the total price                      | ✅      |
| Remove Product from Cart                      | Remove Button           | Click the remove button to delete the product                     | The product should be removed from the cart and the cart total should update | ✅      |
| Apply Discount Code                           | Discount Code Input     | Enter a valid discount code and submit                            | The discount should be applied and reflected in the order total              | ✅      |
| Checkout Process                              | Checkout Button         | Click the 'Proceed to Checkout' button                            | User should be redirected to the checkout page                               | ✅      |
| Display Order Summary                         | Order Summary           | View the total, discount, and final price in the order summary    | Order summary should display item total, discount, and final total           | ✅      |
| Verify Discount Applied                       | Discount Code Input     | Enter a discount code and check if the discount is applied        | Discount should be reflected in the order total                              | ✅      |
| Proceed to Checkout Button                    | Checkout Button         | Click the 'Proceed to Checkout' button                            | User should be redirected to the checkout page                               | ✅      |
| Verify Total Price with Shipping              | Order Total             | Verify total price calculation with shipping costs                | Total price should include product price and shipping cost                   | ✅      |
| Verify Payment Methods Display                | Payment Method Icons    | Check that payment methods are displayed (Visa, MasterCard, etc.) | All payment method icons should be visible (Visa, MasterCard, etc.)          | ✅      |
| Update Quantity with Invalid Number (Failure) | Quantity Input Field    | Enter a negative or zero value and submit                         | An error message should be displayed, and quantity should not update         | ✅      |
| Apply Invalid Discount Code (Failure)         | Discount Code Input     | Enter an invalid discount code and submit                         | An error message should be displayed, and the discount should not apply      | ✅      |
| Proceed to Checkout without Items (Failure)   | Checkout Button         | Click the 'Proceed to Checkout' button with an empty cart         | An error message should be displayed, and checkout should not proceed        | ✅      |

**CHECKOUT**

| Test Case                                          | Element                          | Action                                                            | Expected Outcome                                                       | Result |
| -------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------- | ------ |
| Display Order Summary                              | Order Summary Section            | View the order summary with item and price                        | Order summary should display correct product details and price         | ✅      |
| Verify Product in Order Summary                    | Product Details in Order Summary | Verify the product name, quantity, and price in the summary       | Product details should match the selected items in the order summary   | ✅      |
| Verify Total Price                                 | Order Total                      | Check if total price matches product price and shipping cost      | Total price should include item price and delivery fee                 | ✅      |
| Fill Delivery Information                          | Delivery Information Form        | Fill in all required delivery information fields                  | Delivery information should be validated and accepted                  | ✅      |
| Complete Payment                                   | Payment Form                     | Enter payment details and submit the form                         | Payment should be processed successfully, and the order completed      | ✅      |
| Proceed to Checkout                                | Checkout Button                  | Click the 'Complete Order' button to proceed                      | User should be redirected to the confirmation page                     | ✅      |
| Save Delivery Information                          | Save Info Checkbox               | Select the checkbox to save delivery information to profile       | Delivery information should be saved to the user's profile             | ✅      |
| Verify Payment Methods Display                     | Payment Method Icons             | Check that payment methods are displayed (Visa, MasterCard, etc.) | Payment method icons should be visible and selectable                  | ✅      |
| Invalid Phone Number Format (Failure)              | Phone Number Field               | Enter an incorrectly formatted phone number and submit            | An error message should be displayed for incorrect phone number format | ✅      |
| Missing Required Fields in Delivery Info (Failure) | Delivery Information Form        | Leave required fields (e.g., Full Name, Email) empty              | An error message should appear, indicating missing fields              | ✅      |
| Insufficient Stock (Failure)                       | Stock Availability               | Attempt to order more items than available in stock               | An error message should be displayed for insufficient stock            | ✅      |
| Invalid Payment Details (Failure)                  | Payment Details Field            | Enter invalid or incomplete payment information                   | Payment should be rejected, and an error message should be displayed   | ✅      |

**PROFILE**

| Test Case                             | Element                | Action                                                                       | Expected Outcome                                                                                             | Result |
| ------------------------------------- | ---------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| Edit Personal Details                 | First Name Field       | Enter valid first name and submit                                            | First name is successfully updated.                                                                          | ✅      |
| Edit Personal Details                 | Last Name Field        | Enter valid last name and submit                                             | Last name is successfully updated.                                                                           | ✅      |
| Edit Personal Details (Failure)       | First Name Field       | Enter numbers or special characters in first name field and submit           | Form should display an error message indicating invalid characters are not allowed in the first name field.  | ✅      |
| Edit Personal Details (Failure)       | Last Name Field        | Enter a string longer than 150 characters and submit                         | Form should display an error message indicating that the last name is too long.                              | ✅      |
| Update Shipping Information           | Phone Number Field     | Enter a valid phone number and submit                                        | Phone number is successfully updated.                                                                        | ✅      |
| Update Shipping Information (Failure) | Phone Number Field     | Enter letters or special characters in phone number field and submit         | Form should display an error message indicating invalid characters in the phone number field.                | ✅      |
| Update Shipping Information           | Street Address Field   | Enter a valid street address and submit                                      | Street address is successfully updated.                                                                      | ✅      |
| Update Shipping Information (Failure) | City Field             | Leave the city field blank and submit                                        | Form should display an error message indicating that the city field is required.                             | ✅      |
| Change Password                       | Current Password Field | Enter the correct current password and valid new password twice and submit   | Password should be successfully changed.                                                                     | ✅      |
| Change Password (Failure)             | Current Password Field | Enter the incorrect current password and submit                              | Form should display an error message indicating the current password is incorrect.                           | ✅      |
| Change Password (Failure)             | New Password Field     | Enter different values for the new password and password confirmation fields | Form should display an error message indicating that the two password fields do not match.                   | ✅      |
| Add Item to Wishlist                  | Wishlist Button        | Click on the 'Add to Wishlist' button for a product                          | Item should be successfully added to the wishlist.                                                           | ✅      |
| Add Item to Wishlist (Failure)        | Wishlist Button        | Try adding an out-of-stock item to the wishlist                              | The product is not added to the wishlist, and a message indicating the product is unavailable should appear. | ✅      |
| Delete Account                        | Delete Account Button  | Confirm account deletion and submit                                          | The account should be permanently deleted.                                                                   | ✅      |
| Delete Account (Failure)              | Delete Account Button  | Attempt to delete an account without confirming the action                   | The account should not be deleted, and the user is prompted to confirm the action.                           | ✅      |

**ADMIN**

| Test Case                                     | Element                                        | Action                                                       | Expected Outcome                                                         | Result |
| --------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ | ------ |
| Verify page loads correctly                   | Full page                                      | Open the admin dashboard URL                                 | The admin dashboard should load without errors.                          | ✅      |
| Verify top navigation items                   | Top navigation (cart, wishlist, profile, etc.) | Click on each top navigation item                            | The correct page for each item should load (e.g., Cart, Profile, etc.).  | ✅      |
| Verify correct admin name                     | Top navigation - username                      | Check the username next to the user icon                     | The username 'admin' should appear.                                      | ✅      |
| Verify 'Dashboard' link                       | Sidebar - Dashboard link                       | Click on 'Dashboard'                                         | The admin dashboard summary page should load.                            | ✅      |
| Verify 'Products' link                        | Sidebar - Products link                        | Click on 'Products'                                          | The product management page should load.                                 | ✅      |
| Verify 'Categories' link                      | Sidebar - Categories link                      | Click on 'Categories'                                        | The category management page should load.                                | ✅      |
| Verify 'Genres' link                          | Sidebar - Genres link                          | Click on 'Genres'                                            | The genre management page should load.                                   | ✅      |
| Verify 'Authors' link                         | Sidebar - Authors link                         | Click on 'Authors'                                           | The author management page should load.                                  | ✅      |
| Verify 'Discounts' link                       | Sidebar - Discounts link                       | Click on 'Discounts'                                         | The discounts management page should load.                               | ✅      |
| Verify 'Orders' link                          | Sidebar - Orders link                          | Click on 'Orders'                                            | The orders management page should load.                                  | ✅      |
| Verify 'Today's Metrics' section data display | Today's Metrics section                        | View the metrics for 'New Orders', 'Products Sold', etc.     | Metrics should display correct data for the current day.                 | ✅      |
| Verify 'Overall Metrics' section data display | Overall Metrics section                        | View the metrics for 'Total Sales', 'Registered Users', etc. | The overall metrics should display the correct cumulative data.          | ✅      |
| Verify registration data in 'Today's Metrics' | Today's Metrics - Registrations                | View the 'Registrations Today' metric                        | The correct number of new registrations should display.                  | ✅      |
| Verify 'Total Sales' data                     | Overall Metrics - Total Sales                  | View the 'Total Sales' amount                                | The 'Total Sales' should display the correct amount of cumulative sales. | ✅      |
| Verify 'Stock Utilization' data               | Overall Metrics - Stock Utilization            | View the 'Stock Utilization' percentage                      | The stock utilization percentage should be accurate.                     | ✅      |

**HEADER**

| Test Case                            | Element                 | Action                                           | Expected Outcome                               | Result |
| ------------------------------------ | ----------------------- | ------------------------------------------------ | ---------------------------------------------- | ------ |
| Verify Page Logo Navigation          | Logo                    | Click on the logo                                | Navigates to the homepage                      | ✅      |
| Verify Cart Navigation               | Cart Icon               | Click on the cart icon                           | Navigates to the cart page                     | ✅      |
| Verify Wishlist Navigation           | Wishlist Icon           | Click on the wishlist icon                       | Navigates to the wishlist page                 | ✅      |
| Verify Profile Dropdown              | Profile Dropdown        | Click on the profile dropdown                    | Dropdown menu is displayed                     | ✅      |
| Verify Product Management Navigation | Product Management Link | Click on 'Product Management'                    | Navigates to the product management page       | ✅      |
| Verify Profile Navigation            | Profile Link            | Click on 'Profile'                               | Navigates to the profile page                  | ✅      |
| Verify My Orders Navigation          | My Orders Link          | Click on 'My Orders'                             | Navigates to the orders page                   | ✅      |
| Verify My Wishlist Navigation        | My Wishlist Link        | Click on 'My Wishlist'                           | Navigates to the wishlist page                 | ✅      |
| Verify My Cart Navigation            | Cart Link               | Click on 'My Cart'                               | Navigates to the cart page                     | ✅      |
| Verify Logout Functionality          | Logout Link             | Click on 'Logout'                                | Logs out the user                              | ✅      |
| Verify Main Navigation Bar           | Main Navigation Bar     | View navigation bar                              | Navigation bar is displayed with correct links | ✅      |
| Verify 'All Books' Navigation        | 'All Books' Link        | Click on 'All Books'                             | Navigates to the 'All Books' page              | ✅      |
| Verify 'Special Offers' Navigation   | 'Special Offers' Link   | Click on 'Special Offers'                        | Navigates to the 'Special Offers' page         | ✅      |
| Verify 'About Us' Navigation         | 'About Us' Link         | Click on 'About Us'                              | Navigates to the 'About Us' page               | ✅      |
| Verify Navbar Toggle in Mobile View  | Navbar Toggle           | Click on the navbar toggle button in mobile view | Expands the navigation bar                     | ✅      |


**FOOTER**

| Test Case                                        | Element                         | Action                                                                                                                   | Expected Outcome                                                           | Result |
| ------------------------------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ------ |
| Test Logo and About Section Visibility           | Logo and About Section          | Verify the visibility of the logo and about text                                                                         | The logo and text 'Your cozy corner for books and brews' should be visible | ✅      |
| Test Social Media Links Functionality            | Social Media Links              | Click each social media link (GitHub, Facebook, LinkedIn, Email) and verify they open correctly                          | Each social media link should open the correct platform or email client    | ✅      |
| Test 'We Accept' Icons Display                   | 'We Accept' Icons               | Verify that the 'We Accept' icons (Visa, MasterCard, etc.) are displayed                                                 | 'We Accept' icons (Visa, MasterCard, etc.) should be visible               | ✅      |
| Test Shop Section Links Navigation               | Shop Section Links              | Click each shop section link (Shop All Books, Shipping & Returns, Privacy Policy, Terms of Service) and check navigation | User should be navigated to the correct pages for each shop section link   | ✅      |
| Test Newsletter Subscription Input               | Newsletter Email Input          | Enter email address in the input box                                                                                     | User should be able to enter an email address                              | ✅      |
| Test Newsletter Subscription Button              | Newsletter Subscription Button  | Click the 'Subscribe' button after entering an email                                                                     | Button click should trigger a subscription process                         | ✅      |
| Test Newsletter Error Response for Invalid Email | Newsletter Subscription Error   | Enter an invalid email and click the 'Subscribe' button                                                                  | User should see an error message about invalid email                       | ✅      |
| Test Newsletter Success Response for Valid Email | Newsletter Subscription Success | Enter a valid email and click the 'Subscribe' button                                                                     | User should see a success message confirming subscription                  | ✅      |


**LANDING PAGE**

| Test Case                             | Element                   | Action                                  | Expected Outcome                                                       | Result |
| ------------------------------------- | ------------------------- | --------------------------------------- | ---------------------------------------------------------------------- | ------ |
| Verify Hero Title Display             | Hero Title <h1>           | Check if title is displayed correctly   | Title 'Welcome to Teacup Tales Books' is displayed on the page         | ✅      |
| Verify Hero Subtitle Display          | Hero Subtitle <h2>        | Check if subtitle is displayed          | Subtitle 'Where Every Book is a Steaming Cup of Adventure.' is visible | ✅      |
| Quick Search Form Title Field         | Title <input> field       | Enter valid title and submit            | Search results for the entered title are displayed                     | ✅      |
| Quick Search Form Author Field        | Author <input> field      | Enter valid author and submit           | Search results for the entered author are displayed                    | ✅      |
| Quick Search Form Description Field   | Description <input> field | Enter valid description and submit      | Search results for the entered description are displayed               | ✅      |
| Quick Search Form ISBN Field          | ISBN <input> field        | Enter valid ISBN and submit             | Search results for the entered ISBN are displayed                      | ✅      |
| Quick Search Submit Button            | Submit Button             | Click on the submit button              | Search results are displayed based on the entered data                 | ✅      |
| Hero Image Display                    | Hero Image                | Check if hero image loads               | Hero image is displayed correctly on the page                          | ✅      |
| Category Navigation: Special Offers   | Special Offers <i> icon   | Click on Special Offers icon            | Redirect to Special Offers page                                        | ✅      |
| Category Navigation: Romance          | Romance <i> icon          | Click on Romance icon                   | Redirect to Romance category page                                      | ✅      |
| Category Navigation: History          | History <i> icon          | Click on History icon                   | Redirect to History category page                                      | ✅      |
| Category Navigation: Children's Books | Children's Books <i> icon | Click on Children's Books icon          | Redirect to Children's Books category page                             | ✅      |
| Category Navigation: Mind & Body      | Mind & Body <i> icon      | Click on Mind & Body icon               | Redirect to Mind, Body & Spirit category page                          | ✅      |
| Bestseller Section Display            | Bestseller Books          | Check if bestseller books are displayed | Bestseller books are shown under 'This Month's Bestsellers' section    | ✅      |
| New Arrivals Section Display          | New Arrival Books         | Check if new arrivals are displayed     | New arrival books are shown under 'New Arrivals' section               | ✅      |
| Verify Bestseller Book Links          | Bestseller Book Image     | Click on Bestseller Book Image          | Redirect to the specific product page                                  | ✅      |
| Verify New Arrival Book Links         | New Arrival Book Image    | Click on New Arrival Book Image         | Redirect to the specific product page                                  | ✅      |
| New Arrivals Pricing Display          | New Arrival Prices        | Verify if sale prices are displayed     | Correct sale prices are displayed for new arrival products             | ✅      |
</details><br/>

[Back to top](#contents)



## Role-based Restrictions

The user role based restrictions were tested to ensure that view and functionality reflects the scope of the project.

| Admin                                                   | Test Pass |
| ------------------------------------------------------- | --------- |
| Full access to all resources and features.              | ✅         |
| Can create, read, update, and delete any content.       | ✅         |
| Can manage user roles and permissions.                  | ✅         |
| Access to admin dashboard and settings.                 | ✅         |
| Can view all users data.                                | ✅         |
                                                                   
                                                                 
| Registered User                                         | Test Pass
--------------------------------------------------------- | ---------- |
| Can create, read, update, and delete their own content. | ✅         |
| Cannot manage content created by other users.           | ✅         |
| Can create and manage their own comments.               | ✅         |
| Can purchase products.                                  | ✅         |
| Can manage their own wishlist.                          | ✅         |
| Can manage their own user account.                      | ✅         |
                                                                   
| Visitor                                                 | Test Pass |
--------------------------------------------------------- | ---------- |
| Can only read publicly available content.               | ✅         |
| Cannot create, update, or delete any content.           | ✅         |
| Cannot manage reviews and wishlist.                     | ✅         |
| Cannot make purchases.                                  | ✅         |

[Back to top](#contents)

## Bugs

[Back to top](#contents)

## Browser Compatibility

The deployed project was tested on the most popular browsers for compatibility issues.
No major issues identified. 

[Browser Testing Results](/docs/testing-md/browser-testing.pdf)

## User Story Testing


**Dev Role User Stories**


| User Story                                                                                          | Acceptance Criteria Complete | Notes                                                                                                                  |
| --------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [Adopt Agile Methodology](https://github.com/Indre-V/teacup-tales-bookshop/issues/9)                | ✅                            | Documented in README.md                                                                                                |
| [Design Database Schema](https://github.com/Indre-V/teacup-tales-bookshop/issues/10)                | ✅                            | Database design documented in README.md                                                                                |
| [Create Wireframes](https://github.com/Indre-V/teacup-tales-bookshop/issues/12)                     | ✅                            | Wireframes documented in README.md                                                                                     |
| [Design Visuals](https://github.com/Indre-V/teacup-tales-bookshop/issues/11)                        | ✅                            | Design process documented in README.md                                                                                 |
| [Create Django Project](https://github.com/Indre-V/teacup-tales-bookshop/issues/13)                 | ✅                            | Git Commit [ac72496](https://github.com/Indre-V/teacup-tales-bookshop/commit/ac7249661d208baa77860be3c8624169658ee84b) |
| [Heroku Deployment](https://github.com/Indre-V/teacup-tales-bookshop/issues/39)                     | ✅                            | Git Commit [ffb4bbc](https://github.com/Indre-V/teacup-tales-bookshop/commit/ffb4bbc1bfe635a489edaf516533c9fee18686ad) |
| [Performance Optimization](https://github.com/Indre-V/teacup-tales-bookshop/issues/31)              | ✅                            | Results documented in TESTING.md                                                                                       |
| [Code Validation](https://github.com/Indre-V/teacup-tales-bookshop/issues/37)                       | ✅                            | Results documented in TESTING.md                                                                                       |
| [Comprehensive Project Documentation](https://github.com/Indre-V/teacup-tales-bookshop/issues/36)   | ✅                            | Comprehensive README.md and TESTING.md                                                                                 |
| [User Story Testing](https://github.com/Indre-V/teacup-tales-bookshop/issues/38)                    | ✅                            | Results documented in TESTING.md                                                                                       |
| [Performance and Accessibility Testing](https://github.com/Indre-V/teacup-tales-bookshop/issues/40) | ✅                            | Results documented in TESTING.md                                                                                       |
| [SEO](https://github.com/Indre-V/teacup-tales-bookshop/issues/34)                                   | ✅                            | Results documented in TESTING.md                                                                                       |
| [Facebook Marketing](https://github.com/Indre-V/teacup-tales-bookshop/issues/33)                    | ✅                            | Results documented in TESTING.md                                                                                       |



**Visitor User Stories**

| User Story                                                                                    | Acceptance Criteria Complete | Screenshot/Notes                                                                                            |
| --------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [User Registration](https://github.com/Indre-V/teacup-tales-bookshop/issues/14)               | ✅                            |  <details><summary>Screenshot</summary>![Registration](/docs/testing-md/userstories/user-reg.png)</details> |
| [Newsletter](https://github.com/Indre-V/teacup-tales-bookshop/issues/14)                      | ✅                            |  <details><summary>Screenshot</summary>![Newsletter](/docs/testing-md/userstories/newsletter.png)</details> |
| [Implement Navigation Experience](https://github.com/Indre-V/teacup-tales-bookshop/issues/28) | ✅                            | Summary documented in README.md                                                                             |
| [Visual Consistency](https://github.com/Indre-V/teacup-tales-bookshop/issues/29)              | ✅                            | Summary documented in README.md                                                                             |
| [Accessibility Enhancement](https://github.com/Indre-V/teacup-tales-bookshop/issues/30)       | ✅                            | Test results documented in TESTING.md                                                                       |



**Customer User Stories**

| User Story                                                                                                              | Acceptance Criteria Complete | Screenshot                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [User Login and Logout Functionality](https://github.com/Indre-V/teacup-tales-bookshop/issues/15)                       | ✅                            |  <details><summary>Screenshot</summary>![Log](/docs/testing-md/userstories/login.png)</details>                              |
| [Password Reset](https://github.com/Indre-V/teacup-tales-bookshop/issues/16)                                            | ✅                            |  <details><summary>Screenshot</summary>![Password-Reset](/docs/testing-md/userstories/password-reset.png)</details>          |
| [Profile Management](https://github.com/Indre-V/teacup-tales-bookshop/issues/17)                                        | ✅                            |  <details><summary>Screenshot</summary>![Profile](/docs/testing-md/userstories/profile-view.png)</details>                   |
| [Add a Review](https://github.com/Indre-V/teacup-tales-bookshop/issues/19)                                              | ✅                            |  <details><summary>Screenshot</summary>![Add-Comment](/docs/testing-md/userstories/add-review.png)</details>                 |
| [Manage Reviews](https://github.com/Indre-V/teacup-tales-bookshop/issues/20)                                            | ✅                            |  <details><summary>Screenshot</summary>![Manage-Comment](/docs/testing-md/userstories/manage-reviews.png)</details>          |
| [User Interaction with Products](https://github.com/Indre-V/teacup-tales-bookshop/issues/18)                            | ✅                            |  <details><summary>Screenshot</summary>![User-Interaction](/docs/testing-md/userstories/user-interaction.png)</details>      |
| [Simplify Product Selection](https://github.com/Indre-V/teacup-tales-bookshop/issues/24)                                | ✅                            |  <details><summary>Screenshot</summary>![Advanced Search](/docs/testing-md/userstories/filter.png)</details>                 |
| [Streamline Adding Products to Cart](https://github.com/Indre-V/teacup-tales-bookshop/issues/25)                        | ✅                            |  <details><summary>Screenshot</summary>![Shopping Cart](/docs/testing-md/userstories/cart.png)</details>                     |
| [Secure and Efficient Checkout](https://github.com/Indre-V/teacup-tales-bookshop/issues/26)                             | ✅                            |  <details><summary>Screenshot</summary>!Checkout](/docs/testing-md/userstories/checkout.png)</details>                       |
| [Integrate User Account Features into the Checkout Process](https://github.com/Indre-V/teacup-tales-bookshop/issues/27) | ✅                            |  <details><summary>Screenshot</summary>![User Details Checkout](/docs/testing-md/userstories/address-checkout.png)</details> |
| [Discount Codes](https://github.com/Indre-V/teacup-tales-bookshop/issues/32)                                            | ✅                            |  <details><summary>Screenshot</summary>![Discount](/docs/testing-md/userstories/discount.png)</details>                      |



**Admin User Stories**

| User Story                                                                                        | Acceptance Criteria Complete | Notes                                                                                                             |
| ------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [Administration Content CRUD](https://github.com/Indre-V/teacup-tales-bookshop/issues/41)         | ✅                            |  <details><summary>Screenshot</summary>![Admin CRUD](/docs/testing-md/userstories/admin-crud.png)</details>       |
| [Add Products to the Store](https://github.com/Indre-V/teacup-tales-bookshop/issues/21)           | ✅                            |  <details><summary>Screenshot</summary>![Add Product](/docs/testing-md/userstories/admin-add.png)</details>       |
| [Update Product Details in the Store](https://github.com/Indre-V/teacup-tales-bookshop/issues/22) | ✅                            |  <details><summary>Screenshot</summary>![Edit Product](/docs/testing-md/userstories/admin-edit.png)</details>     |
| [Remove Products from the Store](https://github.com/Indre-V/teacup-tales-bookshop/issues/23)      | ✅                            |  <details><summary>Screenshot</summary>![Delete Product](/docs/testing-md/userstories/admin-delete.png)</details> |



## Lighthouse Testing

Teacup Tales Bookshop was tested in the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and [Microsoft Edge Dev Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/open/?tabs=cmd-Windows) using Lighthouse Testing tool which inspects and scores the website for the following criteria:

* Performance - how quickly a website loads and how quickly users can access it.
* Accessibility - test analyses how well people who use assistive technologies can use your website.
* Best Practices - checks whether the page is built on the modern standards of web development.
* SEO - checks if the website is optimised for search engine result rankings.

All images were compressed and converted to .webp using [tiny.png](https://tinypng.com/) to improve performance scores. Website was tested with extra content to replicate real life scenario.

<details><summary><b>Lighthouse Test Results</b></summary>

| Page                  | Status          | Size    | Result | Screenshot                                                                     | Notes                                                |
| --------------------- | --------------- | ------- | ------ | ------------------------------------------------------------------------------ | ---------------------------------------------------- |
| Home                  | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/logged-out-home-desktop.png )        |                                                      |
| Home                  | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/logged-in-home-desktop.png )         |                                                      |
| Home                  | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/logged-out-home-mobile.png )         |                                                      |
| Home                  | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/logged-in-home-mobile.png )          |                                                      |
| All Books             | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-products-desktop.png )       |                                                      |
| All Books             | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-products-desktop.png )      |                                                      |
| All Books             | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-products-mobile.png )        |                                                      |
| All Books             | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-products-mobile.png )       |                                                      |
| Add product           | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-add-product-mobile.png )    | Url field affecting accessibility score              |
| Add product           | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-add-product-desktop.png )   | Url field affecting accessibility score              |
| Profile - Orders      | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-profile-orders-mobile.png ) |                                                      |
| Profile - Orders      | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-profile-order-desktop.png ) | SEO flagging order links                             |
| Profile - Wishlist    | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-prof-wishlist-desktop.png ) |                                                      |
| Profile - wishlist    | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-prof-favs-mobile.png )      |                                                      |
| Profile - Information | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/prof-info-desktop.png )              |                                                      |
| Profile - Information | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/prof-info-mobile.png )               |                                                      |
| Change-Password       | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/change-pass-desktop.png )            |                                                      |
| Change-Password       | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/change-pass-mobile.png )             |                                                      |
| Delete-Account        | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/del-acc-desktop.png )                |                                                      |
| Delete-Account        | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/del-acc-mobile.png )                 |                                                      |
| Product-Detail        | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-products-dets-desktop.png ) |                                                      |
| Product-Detail        | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-products-dets-mobile.png )  |                                                      |
| Product-Detail        | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-product-dets-desktop.png )   |                                                      |
| Product-Detail        | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-product-dets-mobile.png )    |                                                      |
| Edit-review           | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-edit-review-mobile.png )    |                                                      |
| Edit-review           | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-edit-review-desktop.png )   |                                                      |
| About                 | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-about-desktop.png )          |                                                      |
| About                 | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-about-desktop.png )         |                                                      |
| About                 | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-about-mobile.png )           |                                                      |
| About                 | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-about-mobile.png )          |                                                      |
| Search-Results        | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-search-desktop.png )         |                                                      |
| Search-Results        | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-search-desktop.png )        |                                                      |
| Search-Results        | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-search-mobile.png )          |                                                      |
| Search-Results        | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-search-mobile.png )         |                                                      |
| Cart                  | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-cart-desktop.png )           |                                                      |
| Cart                  | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-cart-desktop.png )          |                                                      |
| Cart                  | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-cart-mobile.png )            |                                                      |
| Cart                  | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-cart-mobile.png )           |                                                      |
| Registration          | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-user-reg-mobile.png )        |                                                      |
| Registration          | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-user-reg-desktop.png )       |                                                      |
| LogIn                 | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-user-login-mobile.png )      | Allauth template flagging background error           |
| LogIn                 | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-user-login-desktop.png )     | Allauth template flagging background error           |
| Shipping & Returns    | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-shipping-mobile.png )        |                                                      |
| Shipping & Returns    | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-shipping-desktop.png )       |                                                      |
| Shipping & Returns    | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-shipping-mobile.png )       |                                                      |
| Shipping & Returns    | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-shipping-desktop.png )      |                                                      |
| Privacy Policy        | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-privacy-mobile.png )         |                                                      |
| Privacy Policy        | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-privacy-desktop.png )        |                                                      |
| Privacy Policy        | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-privacy-mobile.png )        |                                                      |
| Privacy Policy        | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-privacy-desktop.png )       |                                                      |
| Terms of Service      | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-terms-desktop.png )          |                                                      |
| Terms of Service      | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-terms-mobile.png )           |                                                      |
| Terms of Service      | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-terms-desktop.png )         |                                                      |
| Terms of Service      | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-terms-mobile.png )          |                                                      |
| Special Offers        | Visitor         | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-offers-desktop.png )         |                                                      |
| Special Offers        | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-offers-desktop.png )        |                                                      |
| Special Offers        | Visitor         | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/visitor-offers-mobile.png )          |                                                      |
| Special Offers        | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-offers-mobile.png )         |                                                      |
| Admin Dashboard       | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-dashboard-mobile.png )      |                                                      |
| Admin Dashboard       | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-dashboard-desktop.png )     |                                                      |
| Checkout              | Registered User | Mobile  | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-checkout-mobile.png )       | Country Field flag image and Stripe affecting scores |
| Checkout              | Registered User | Desktop | ✅      | ![screenshot](/docs/testing-md/lighthouse/reg-user-checkout-desktop.png )      | Country Field flag image affecting scores            |

</details><br/>

[Back to top](#contents)


## Accessibility Testing

Cccessibility scores were high on Lighthouse, however I retested the page.
[WAVE](https://wave.webaim.org/) online tool was used to check terminal colour contrast. All tests were passed.

While building the application, the general principles of accessibility were adhered to: 

- Using clear instructions
- Validating inputs before moving on to the next step
- Testing the page to make sure it does not affect performance from user input
- Using ARIA labels

![WAVE](/docs/testing-md/summary.png)

[Back to top](#contents)



