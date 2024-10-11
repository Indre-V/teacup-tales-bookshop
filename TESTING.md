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

[Back to top](#contents)

## Manual Testing

In addition to using `unittest`, extensive manual testing was performed on the application. Each feature was verified against success criteria. Where applicable, negative testing was conducted by providing invalid or unexpected inputs to assess the application's robustness in handling errors and exceptions.

<details><summary><b>Manual Testing Results</b></summary>

</details><br/>

[Back to top](#contents)



## Role-based Restrictions

[Back to top](#contents)

## Bugs

## Browser Compatibility

The deployed project was tested on the most popular browsers for compatibility issues.
No major issues identified. 

[Browser Testing Results](/docs/testing-md/browser-testing.pdf)

## User Story Testing

## Lighthouse Testing

Teacup Tales Bookshop was tested in the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and [Microsoft Edge Dev Tools](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/open/?tabs=cmd-Windows) using Lighthouse Testing tool which inspects and scores the website for the following criteria:

* Performance - how quickly a website loads and how quickly users can access it.
* Accessibility - test analyses how well people who use assistive technologies can use your website.
* Best Practices - checks whether the page is built on the modern standards of web development.
* SEO - checks if the website is optimised for search engine result rankings.

All images were compressed and converted to .webp using [tiny.png](https://tinypng.com/) to improve performance scores. Website was tested with extra content to replicate real life scenario.

<details><summary><b>Lighthouse Test Results</b></summary>

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



