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


| \*\*Dev Role User Stories\*\*                                                                       |                              |                                                                                                                        |
| --------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
|                                                                                                     |                              |                                                                                                                        |
| User Story                                                                                          | Acceptance Criteria Complete | Notes                                                                                                                  |
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


| \*\*Visitor User Stories\*\*                                                                  |                              |                                                                                                             |
| --------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
|                                                                                               |                              |                                                                                                             |
| User Story                                                                                    | Acceptance Criteria Complete | Screenshot/Notes                                                                                            |
| [User Registration](https://github.com/Indre-V/teacup-tales-bookshop/issues/14)               | ✅                            |  <details><summary>Screenshot</summary>![Registration](/docs/testing-md/userstories/user-reg.png)</details> |
| [Newsletter](https://github.com/Indre-V/teacup-tales-bookshop/issues/14)                      | ✅                            |  <details><summary>Screenshot</summary>![Newsletter](/docs/testing-md/userstories/newsletter.png)</details> |
| [Implement Navigation Experience](https://github.com/Indre-V/teacup-tales-bookshop/issues/28) | ✅                            | Summary documented in README.md                                                                             |
| [Visual Consistency](https://github.com/Indre-V/teacup-tales-bookshop/issues/29)              | ✅                            | Summary documented in README.md                                                                             |
| [Accessibility Enhancement](https://github.com/Indre-V/teacup-tales-bookshop/issues/30)       | ✅                            | Test results documented in TESTING.md                                                                       |


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


| \*\*Admin User Stories\*\*                                                                        |                              |                                                                                                                   |
| ------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
|                                                                                                   |                              |                                                                                                                   |
| User Story                                                                                        | Acceptance Criteria Complete | Notes                                                                                                             |
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



