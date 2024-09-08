# Teacup Tales Bookstore

![Main Image](/docs/readme-md/main-image.png)

[Deployed Link]()




- [Agile Methodology](#agile-methodology)
  * [Overview](#overview)
  * [MoSCoW Prioritization](#moscow-prioritization)
  * [GitHub Projects](#github-projects)
  * [EPICS](#epics)
  * [User Stories](#user-stories)
  * [Developer Stories](#developer-stories)
  * [Visitor Stories](#visitor-stories)
  * [Registered User Stories](#registered-user-stories)
  * [Admin User Stories](#admin-user-stories)
- [Website Goals and Objectives](#website-goals-and-objectives)
- [Target Audience](#target-audience)
- [Wireframes](#wireframes)
- [Database Schema](#database-schema)
- [Design Choices](#design-choices)
  * [Typography](#typography)
  * [Colour Scheme](#colour-scheme)
  * [Images](#images)
  * [Responsiveness](#responsiveness)
- [Security Measures and Protective Design](#security-measures-and-protective-design)
  * [User Authentication](#user-authentication)
  * [Password Management](#password-management)
  * [Form Validation](#form-validation)
  * [Database Security](#database-security)
- [Features](#features)

- [Django Admin Portal](#django-admin-portal)
- [Future Features](#future-features)
    + [Enhanced User Profiles](#enhanced-user-profiles)
    + [Advanced Insights Management](#advanced-insights-management)
    + [Community Interaction](#community-interaction)
    + [Content Discovery](#content-discovery)
    + [Accessibility and Inclusivity](#accessibility-and-inclusivity)
- [Deployment](#deployment)
  * [To deploy the project to Heroku](#to-deploy-the-project-to-heroku)
  * [To fork the project](#to-fork-the-project)
  * [To clone the project](#to-clone-the-project)
- [Testing](#testing)
- [Technology](#technology)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Python Libraries](#python-libraries)
  * [Programs](#programs)
- [Credits](#credits)
- [Disclaimer](#disclaimer)


## Agile Methodology

### Overview

Agile methodology is a project management approach that focuses on flexibility, teamwork, and making steady progress toward a clear objective. It is especially effective in software development, where requirements and solutions evolve through the joint efforts of self-organizing, cross-functional teams. Agile methodologies strive to deliver small, incremental product updates that enhance quality and allow for quick adaptation to changing needs.


### MoSCoW Prioritization

The MoSCoW prioritization technique is a framework for assessing the importance of different features and tasks within a project. It classifies items into four categories: Must Have, Should Have, Could Have, and Won't Have. This approach aids in effective time management by ensuring that the most essential features are prioritized and completed first.

### GitHub Projects

GitHub Projects provides a way to manage tasks and monitor progress using project boards. Each board represents an EPIC, with columns that track the status of tasks, such as To Do, In Progress, On Hold, Done, and Bugs. Tasks are organized with labels indicating the user, priority, and sprint.

![Kanban Board](/docs/readme-md/kanban-board.png)

### EPICS

An Epic is a large segment of work broken down into smaller user stories. In this project, each Epic represents a significant component of the platform's development, ensuring all necessary functionalities are fully covered.

- [EPIC 1: Design Planning](https://github.com/users/Indre-V/projects/6/views/1?pane=issue&itemId=78411335)
- [EPIC 2: Admin and Store Management](https://github.com/users/Indre-V/projects/6/views/1?pane=issue&itemId=78414830)
- [EPIC 3: User Account Management](https://github.com/users/Indre-V/projects/6/views/1?pane=issue&itemId=78415204)
- [EPIC 4: User Engagement](https://github.com/users/Indre-V/projects/6?pane=issue&itemId=78415617)
- [EPIC 5: Seamless Checkout Experience](https://github.com/users/Indre-V/projects/6?pane=issue&itemId=78496164)
- [EPIC 6: User Experience Optimization](https://github.com/users/Indre-V/projects/6/views/1?pane=issue&itemId=78498476)
- [EPIC 7: SEO & Marketing](https://github.com/users/Indre-V/projects/6/views/1?pane=issue&itemId=78499191)
- [EPIC 8: Quality Assurance and Documentation](https://github.com/users/Indre-V/projects/6/views/1?pane=issue&itemId=78499407)

### User Stories

With an emphasis on delivering a seamless user experience, the goal of this project is to provide a comprehensive platform that serves both visitors and registered users. The platform will allow for the development and maintenance of content, present developer profiles, and provide opportunities for interaction.  The following user stories outline the essential functionalities and the rationale behind them.

*************************************
### Developer Stories

- As a **developer**, I want to **create wireframes** so that I can **visually represent the layout and structure of the application.**

- As a **developer**, I want to **adopt Agile methodology** so that **I can deliver high quality product that meets the needs of the user.**

- As a **developer**, I want to **design a database schema**  to efficiently store and manage platform content, ensuring optimal performance, scalability, and flexibility.**

- As a **developer**, I want to **create visually engaging and responsive designs** so that **users can easily navigate the website and access relevant information.**

- As a **developer**, I want to **install and add basic configurations to Django** so that **I can create a working application**.

- As a **developer**, I want to **the platform to load quickly and respond swiftly to user interactions** so that **users can have a seamless experience.**

- As a **developer** , I want to be **able to share the business on Facebook** so that **I can reach and market to a larger audience.**

- As a **developer**, I want to **improve the website's search engine optimization (SEO)** so that **the website can rank higher in search engine results and attract more organic traffic.**

- As a **developer**, I want to **maintain thorough documentation** so that **code is maintained seamlessly in future.**

- As a **developer**, I want to **ensure that all syntax errors are identified and resolved during the code validation process** so that **the code is free from syntax-related issues.**

- As a **developer**, I want to **ensure that user stories are thoroughly tested** so that **they meet acceptance criteria and deliver the expected functionality.**

- As a **developer**, I want to **deploy the application to Heroku** so that **it is accessible to users online.**

- As a **developer**, I want to **ensure that application meets performance and accessibility standards** so that **provides a seamless experience for all users and performs optimally.**

*************************************************************
### Visitor Stories

- As a **visitor**, I want to **able to register an account** so **I can create an account.**

- As a **visitor**, I want to **navigate through the platform effortlessly,** so that **I can find relevant sections and features intuitively.**

- As a **visitor**, I want to **visual elements across the platform to be consistent** so that **I can have a cohesive and pleasant user interface experience.**

- As a **visitor**, I want the **accessibility features to be improved** so that **to maintain equal access and usability for all users, including those with disabilities.**

- As a **visitor**, I want to **subscribe to a newsletter** so that I can **receive updates, promotions, and valuable content directly to my inbox.**

*************************************************************
### Admin User Stories

- As an **admin user**, I want **the ability to add new products to my store, so I can keep my inventory up-to-date efficiently.**

- As an **admin user**, I want **the ability to update product details, including prices, descriptions, images, and other attributes,** to ensure that **product information remains accurate and current on the store's website.**

- As an **admin user**, I want the **ability to remove products from the store**, so that **I can keep the inventory current and eliminate any outdated or discontinued items.**

- As an **admin user**, I want **the ability to perform all CRUD (Create, Read, Update, Delete) operations** so that **manually manage, control and edit content**.


*************************************************************
### Customer

- As a **customer**, I want to **be able to log in and out of my account** so that **I can use the platform.**

- As a **customer**, I want to **to be able to reset my password** so that **I do not loose access to my account.**

- As a **customer**, I want to **manage my profile** so that **I have control of the information held on the platform.**

- As a **customer**, I want **the ability to interact with bookshop listings by providing star ratings, adding products to my favorites**, so that **I can express my opinions, keep track of my favorite books.**

- As a **customer**, I want to **to be able to comment on listings** so that **provide feedback to other customers.**

- As a **customer**, I want to **to be able to delete and edit comments** so that **I can control my engagement on the platform.**

- As a **customer**, I want an **intuitive and efficient way to select products**, so that **I can easily find and choose the items I want to purchase.**

- As a **customer**, I want to **add products to my cart quickly and easily**, so that **I can efficiently manage my selected items before proceeding to checkout.**

- As a **customer**, I want **a secure and efficient checkout process**, so that **I can complete my purchase confidently and without unnecessary delays.**

- As a **customer**, I want **my account information to be seamlessly integrated into the purchasing and checkout process**, so that **I can enjoy a personalized and efficient shopping experience.**

- As a **customer**, I want to **apply discount codes during checkout** so that **I can receive a discount on my purchase.**

## Website Goals and Objectives

* **Enhance User Experience:**
	 - Design a user-friendly interface that is intuitive, visually appealing, and easy to navigate.
	 - Ensure the platform is fully responsive and accessible on all devices, including desktops, tablets, and smartphones.
* **Facilitate Developer Showcase:**
	- Enable registered users to create, edit, and manage posts and comments easily.
	- Introduce features that promote user engagement, such as the ability to like, favorite, and share content.
* **Optimize Performance and Accessibility:**
  - Fine-tune the platform for fast loading times and quick responses to user actions.
  - Adhere to accessibility standards to ensure an inclusive experience for all users.
 * **Support Continuous Improvement and Scalability:**
	- Employ Agile development methodologies to deliver high-quality features and updates continuously.
	- Architect the database and infrastructure to efficiently handle increased traffic and user growth.
* **Ensure Security and Reliability:**
	- Implement strong authentication and authorization protocols to protect user data.
	- Conduct regular code validation and security testing to maintain a stable, secure application.
* **Streamline Payment and Checkout:**
	- Develop a smooth and secure payment process to enhance the checkout experience.
	- Provide multiple payment options and ensure compliance with payment security standards.
* **Encourage Community Engagement and Feedback:**
	- Create channels for users to provide feedback, report issues, and suggest enhancements.
	- Actively respond to user feedback and integrate improvements to continually refine the platform.

## Target Audience

 - Casual Shoppers
 - Book Enthusiasts
 - Independent Authors and Publishers
 - Accessibility-Focused Users


## Wireframes

The wireframes for the platform provide a visual representation of the layout and structure of the application. They outline the placement of key elements such as navigation menus, user profiles, content areas, and interactive features. The wireframes ensure a cohesive and intuitive user interface, guiding the design and development process. After the extensive testing was conducted, naturally there are some deviations from wireframes in the live version of the platform.

[Wireframes](/docs/readme-md/wireframes.pdf "Wireframes")

[Back to top](#contents)

## Database Schema

The database schema outlines the structure and relationships between key tables for the platform.

This schema was generated using [dbdiagram.io](https://dbdiagram.io/).


![Database Schema](/docs/readme-md/database-schema.png)

[Back to top](#contents)

## Design Choices

### Typography

 [Lora](https://fonts.google.com/specimen/Lora?query=lora) was chosen as the primary font.
Lora is a modern serif typeface with calligraphic roots that balances traditional elegance with a contemporary touch. It features slightly rounded letterforms, which give it a friendly and approachable appearance while maintaining excellent readability on both screens and printed materials.

### Colour Scheme

The color scheme warm, earthy tones with deep, contrasting hues to create a welcoming and sophisticated ambiance that resonates with book lovers. The palette features a mix of soft neutrals, rich browns, deep blues, and accents of warm shades, reflecting the cozy, intimate feel of a traditional bookstore while maintaining a modern, stylish look.

-   **Warm Neutrals and Earth Tones**: These provide a soft, comfortable backdrop that is easy on the eyes and ideal for extended reading sessions. They evoke feelings of warmth, tranquility, and familiarity, creating an inviting environment for browsing and exploring books.
    
-   **Deep, Rich Accents**: Darker shades add depth and contrast to the design, highlighting key elements such as headings, call-to-action buttons, and important navigation items. These colors ground the palette, providing a sense of structure and sophistication.
    
-   **Cool, Calm Blues**: The inclusion of cooler hues adds balance and a refreshing contrast to the warm tones. These colors convey trustworthiness and reliability, aligning with the bookstore's goal of providing a seamless and enjoyable shopping experience.
    
-   **Subtle Highlights**: Lighter shades are used for backgrounds, cards, and secondary elements to keep the layout light and airy. They help create a clean and uncluttered look, ensuring the content remains the focal point.
    
Overall, this color scheme balances warmth with contrast, creating a visually appealing and comfortable atmosphere that enhances the browsing and reading experience for users.

![Coolors Scheme](/docs/readme-md/color-scheme.png)


[Back to top](#contents)

### Images

Combination of images sourced from [Leonardo](https://leonardo.ai/ "Leonardo AI") and [Amazon](https://amazon.com). All images sourced from Leonardo AI are available under free licenses, allowing for their use in commercial projects without attribution. This ensures compliance with copyright laws and provides assurance regarding the legal usage of the images on the website. The product images were obtained from Amazon. However, this platform will not be producing any financial gains. 

[Back to top](#contents)

## Security Measures and Protective Design

### User Authentication

- Django's `LoginRequiredMixin` is used to ensure that any requests to access secure pages by non-authenticated users are redirected to the login page.
- Django's `UserPassesTestMixin` is used to limit access based on certain permissions, ensuring users can only edit/delete content they authored. If the user doesn't pass the test, they are shown an HTTP 403 Forbidden error.

### Password Management

- Use Django's built-in password management tools to ensure passwords are hashed and stored securely.
- Enforce strong password policies to enhance user account security.

### Form Validation

If incorrect or empty data is added to a form, the form won't submit, and a warning will appear to the user informing them which field raised the error.

### Database Security

- The database URL and secret key are stored in the `env.py` file to prevent unwanted connections to the database. This setup was implemented before the first push to GitHub.
- Cross-Site Request Forgery (CSRF) tokens are used on all forms throughout the site to enhance security.

[Back to top](#contents)

## E-Commerce Business Model

Teacup Tales operates as an online bookshop, leveraging an e-commerce business model to sell books directly to customers through its website. The model is designed to provide a seamless and personalized shopping experience while catering to a diverse audience of book lovers.

Key components of the Teacup Tales business model include:

1.  **Direct-to-Consumer Sales**: Teacup Tales offers a wide range of books directly to customers, bypassing intermediaries. This approach allows for competitive pricing, higher profit margins, and a more customized shopping experience.
    
2.  **Diverse Product Range**: The shop stocks an extensive selection of books, including fiction, non-fiction, children's literature, rare editions, and niche genres. Additionally, it offers literary-themed merchandise, such as bookmarks, tote bags, and gift cards.
    
3.  **Digital Marketing and SEO**: Teacup Tales employs various digital marketing strategies, including search engine optimization (SEO), content marketing, social media engagement, and email campaigns, to attract and retain customers and increase online visibility.
    
4.  **Logistics and Fulfillment**: The business focuses on efficient inventory management, order processing, and delivery logistics to ensure prompt, reliable shipping. Strategic partnerships with shipping providers help maintain a smooth fulfillment process.
    
5.  **Customer Engagement and Retention**: Teacup Tales fosters a community of readers by offering personalized book recommendations, exclusive author interviews, book reviews, and a loyalty program, aiming to build long-term customer relationships and encourage repeat purchases.
    

This business model enables Teacup Tales to reach a broad audience, minimize overhead costs, and provide an enjoyable, convenient shopping experience for readers around the world.

## Marketing Strategies

### Search Engine Optimisation

To enhance the Teacup Tales visibility and ranking on Google, a comprehensive SEO strategy was developed using tools such as [MOZ](https://moz.com/) and [QuestionDB](https://questiondb.io) to identify relevant keywords for meta tags, alt texts, and content elements.

![MOZ keyword search](/docs/readme-md/moz-kw-dashboard.JPG) ![QuestionDB keyword search](/docs/readme-md/questionDB-questions.JPG)

Based on this research, a mix of short and long-tail keywords were selected to target both specific and broad search queries:

-   online bookstore
-   buy books online
-   best online bookshop
-   novels for sale
-   literary gifts
-   children's books online
-   fiction and non-fiction books
-   rare and antique books
-   personalized book recommendations
-   bookshop for book lovers

### **SEO Strategies Implemented**

1.  **Effective Use of Headings:**
    -   Utilize `<span>` for the bookshop title in the header/navigation, and strategically place `<h1>` tags with relevant keywords to enhance keyword prominence.
    -   Incorporate `<h2>` tags for promotional keywords to improve search relevance.
2.  **Keyword Emphasis:**
    -   Use the `<strong>` HTML element to highlight important short and long-tail keywords throughout the content. This not only provides visual emphasis but also signals their semantic importance to search engines.
3.  **Image Optimization:**
    -   Apply keyword-rich and descriptive alt texts and filenames to all images, ensuring they are relevant to the content and improve searchability.
4.  **Optimize External Links:**
    -   Add the `rel="noopener nofollow"` attribute to social media and external links, which prevents search engines from considering these links when evaluating the site's ranking.
    ![External links noopener ](/docs/readme-md/facebook-nofollow-rel.JPG)

5.  **Sitemap Inclusion:**
    -   Generate and include a `sitemap.xml` file to guide search engine crawlers in indexing the site effectively.
    
    ![SEO sitemap.xml ](/docs/readme-md/sitemap-xml.JPG)
6.  **Control Search Engine Crawling:**
    -   Use a `robots.txt` file to manage and control the behavior of search engine bots while they crawl the site.
    
    ![SEO robots.txt ](/docs/readme-md/robots-txt.JPG)
    

These strategies will be continuously refined and improved over time, aiming to increase the bookshop's ranking on Google and attract more organic traffic to the website.

### Social Media

Teacup Tales will leverage Facebook as a primary platform for engaging with its audience and promoting its online bookshop. The strategy includes the following key components:

1.  **Content Sharing:**    
    -   Post a variety of content, including book recommendations, new arrivals, promotions, literary news, and behind-the-scenes looks at Teacup Tales. This keeps the audience informed and engaged.
2.  **Community Engagement:**    
    -   Foster a sense of community by encouraging interactions through comments, likes, and shares. Respond promptly to customer inquiries and feedback to build relationships and trust.
3.  **Promotional Campaigns:**    
    -   Run targeted ad campaigns to reach potential customers based on their interests, demographics, and browsing behavior. Highlight special offers, book sales, and exclusive events to drive traffic to the website.
4.  **Events and Announcements:**
    -   Use Facebook Events to promote book launches, author signings, and other special events. Keep followers updated on important announcements and store news.
5.  **User-Generated Content:**    
    -   Encourage customers to share their reading experiences, reviews, and photos with Teacup Tales products. Feature user-generated content to build credibility and create a more personal connection with the audience.
6.  **Analytics and Insights:**    
    -   Monitor Facebook Insights to track the performance of posts, ads, and overall engagement. Use this data to refine the strategy, optimize content, and improve outreach efforts.

By focusing on these elements, Teacup Tales will effectively utilize Facebook to enhance brand visibility, engage with readers, and drive traffic to its online bookshop.

### Newsletter Marketing

Teacup Tales will use Mailchimp to manage and send newsletters to keep subscribers updated and engaged. Here’s how it will work:

1.  **Build Subscriber List:**    
    -   Collect email addresses through sign-up forms on the website and social media. Organize subscribers into groups for targeted messaging.
2.  **Create Content:**    
    -   Design newsletters with book recommendations, special offers, and store updates using Mailchimp’s easy-to-use templates.
3.  **Schedule Newsletters:**    
    -   Plan regular newsletters (e.g., weekly or monthly) to keep readers informed and interested.
4.  **Automate Emails:**    
    -   Set up automated emails to welcome new subscribers, thank customers after purchases, and send personalized book suggestions.
5.  **Track Results:**    
    -   Monitor how newsletters perform with Mailchimp’s reports on open rates, clicks, and other key metrics. Use this information to improve future emails.
6.  **Test and Personalize:**    
    -   Test different email elements to see what works best and personalize content based on subscriber preferences.

Using Mailchimp helps Teacup Tales stay connected with readers, promote new books and events, and drive traffic to the online shop.

[Back to top](#contents)

## Features

### Custom Error Pages

- **400 Bad Request** - The platform is unable to process this request.
- **403 Page Forbidden** - It seems user trying to access restricted content. Please log out and sign in to the appropriate account.
- **404 Page Not Found** - The page user is looking for doesn't exist.
- **500 Server Error** - The platform is currently experiencing technical difficulties and cannot process this request.

<details><summary><b>Error View</b></summary>

![Error 400](/docs/readme-md/features/error400.png)
![Error 403](/docs/readme-md/features/error403.png)
![Error 404](/docs/readme-md/features/error404.png)
![Error 500](/docs/readme-md/features/error500.png)
</details><br/>

[Back to top](#contents)

## Django Admin Portal 

Django Admin Portal allows superuser to manage content and users of the website. The admin view is customized to reflect the scope of this project. 

![Django Admin Portal](/docs/readme-md/features/admin-view.png)

[Back to top](#contents)

## Future Features


#### Content Discovery
- **Advanced Search Filters:** Improve search functionality with filters for categories, tags, popularity, and date ranges.
- **Recommendations:** Develop a recommendation engine that suggests insights based on user interests and past interactions.

#### Accessibility and Inclusivity
- **Multi-language Support:** Offer the platform in multiple languages to cater to a global audience.
- **Accessibility Enhancements:** Further improve accessibility features, such as screen reader compatibility, keyboard navigation, and customizable font sizes.

[Back to top](#contents)

## Deployment

### AWS Cloud Service

Teacup Tales uses Amazon Web Services (AWS) to store static and media files securely in the cloud, ensuring fast and reliable access for our users.

**To integrate AWS, follow steps:**

#### **1. Create and Configure an S3 Bucket**

1.  **Access AWS:**
    
    -   Go to [aws.amazon.com](https://aws.amazon.com/) and log in to your AWS Management Console.
2.  **Create an S3 Bucket:**
    
    -   Search for "S3" in the AWS Management Console and create a new bucket.
    -   Name the bucket to match your Heroku app name and select the region closest to your target audience.
3.  **Set Public Access and Ownership:**
    
    -   Uncheck the "Block all public access" option and acknowledge that the bucket will be public (required for compatibility with Heroku).
    -   Under "Object Ownership," ensure "ACLs enabled" and "Bucket owner preferred" are selected.
4.  **Enable Static Website Hosting:**
    
    -   In the "Properties" tab, enable static website hosting.
    -   Set `index.html` as the index document and `error.html` as the error document, then click "Save."
5.  **Configure CORS (Cross-Origin Resource Sharing):**
    
    -   In the "Permissions" tab, add the following CORS configuration:
    
    json
    
    Copy code
    
    `[
      {
        "AllowedHeaders": ["Authorization"],
        "AllowedMethods": ["GET"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
      }
    ]` 
    
    -   Copy your bucket's **ARN** (Amazon Resource Name).
6.  **Add a Bucket Policy:**
    
    -   Go to the "Bucket Policy" tab and click on the "Policy Generator" link.
    -   Configure the policy:
        -   **Policy Type:** S3 Bucket Policy
        -   **Effect:** Allow
        -   **Principal:** *
        -   **Actions:** `s3:GetObject`
        -   **ARN:** Paste your bucket's ARN
    -   Click "Add Statement" and "Generate Policy."
    -   Copy the generated policy and paste it into the "Bucket Policy Editor":
    
    json
    
    Copy code
    
    `{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
      ]
    }` 
    
    -   Ensure the `Resource` field ends with `/*` and click "Save."
7.  **Adjust Access Control List (ACL):**
    
    -   In the "Access Control List" (ACL) section, click "Edit" and enable "List" for Everyone (public access). Accept the warning prompt.
    -   If the edit option is disabled, ensure the "Object Ownership" settings have ACLs enabled.

#### **2. Configure IAM (Identity and Access Management):**

1.  **Create a User Group:**
    
    -   Navigate to the IAM service and select "User Groups."
    -   Click "Create New Group," and name it appropriately (e.g., `group-teacup-tales`).
2.  **Attach Policies to the Group:**
    
    -   Select the newly created group and go to the "Permissions" tab.
    -   Click "Add Permissions" > "Attach Policies."
    -   In the "JSON" tab, click "Import Managed Policy" and search for `AmazonS3FullAccess`.
    -   Import the policy and modify it to limit access to your specific bucket:
    
    json
    
    Copy code
    
    `{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": "s3:*",
          "Resource": [
            "arn:aws:s3:::your-bucket-name",
            "arn:aws:s3:::your-bucket-name/*"
          ]
        }
      ]
    }` 
    
    -   Click "Review Policy" and name it (e.g., `policy-teacup-tales`), then click "Create Policy."
3.  **Add Users and Assign Permissions:**
    
    -   Go back to "User Groups," select your group, and click "Attach Policy."
    -   Select your custom policy (e.g., `policy-teacup-tales`) and attach it.
    -   Click "Add User" and name it appropriately (e.g., `user-teacup-tales`).
    -   Select "Programmatic Access" and add the user to your group.
    -   Download the CSV file containing the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

#### **3. Final AWS Setup and Heroku Integration:**

1.  **Update Heroku Configurations:**
    
    -   Remove `DISABLE_COLLECTSTATIC` from Heroku Config Vars to enable AWS management of static files.
2.  **Create Media Directory:**
    
    -   Within your S3 bucket, create a new folder named `media`.
    -   Upload your media files into this folder and set "Public read access."
3.  **Security Reminder:**
    
    -   Ensure all sensitive information (like AWS credentials) is securely stored and not hard-coded into your source code.

----------

***Summary***

These steps integrate AWS S3 with your Heroku-hosted application, enabling efficient management of static and media files in a secure and scalable cloud environment. Proper configuration ensures that your content is readily accessible while adhering to best practices in cloud security and management.

### Stripe

Teacup Tales utilizes Stripe as its primary payment gateway to securely process e-commerce transactions. Stripe provides a reliable and scalable solution for handling payments, ensuring a seamless checkout experience for our customers.

#### **Steps for Stripe Integration:**

1.  **Create a Stripe Account:**
    
    -   Go to [stripe.com](https://stripe.com) and create an account. Log in to your Stripe dashboard.
2.  **Obtain API Keys:**
    
    -   From your Stripe dashboard, locate the "API Keys" section under "Developers."
    -   Retrieve the following keys:
        -   **STRIPE_PUBLIC_KEY**: Your Publishable Key (starts with `pk`)
        -   **STRIPE_SECRET_KEY**: Your Secret Key (starts with `sk`)
    -   These keys will be used to authenticate your application with Stripe.
3.  **Configure Webhooks for Payment Events:**
    
    -   To handle scenarios where a user may close the payment page prematurely, set up Stripe Webhooks to receive real-time payment updates.
    -   In your Stripe dashboard:
        -   Navigate to "Developers" and select "Webhooks."
        -   Click "Add Endpoint."
        -   Enter your endpoint URL (e.g., `https://teacup-tales.herokuapp.com/checkout/wh/`).
        -   Select "Receive all events" to capture all relevant payment events.
        -   Click "Add Endpoint" to complete the process.
    -   This will generate a new key:
        -   **STRIPE_WH_SECRET**: Your Webhook Signing Secret (starts with `wh`).

#### **Testing Stripe Payments:**

1.  **Test Mode:**
    
    -   Stripe provides a test mode to simulate payment transactions.
    -   Use the following test card details for interactive testing:
        -   **Card Number:** `4242 4242 4242 4242`
        -   **Expiry Date:** Any valid future date (e.g., `12/34`)
        -   **CVC:** Any three-digit number (or four digits for American Express)
        -   **Other Fields:** Use any value for other fields.
2.  **Security Reminder:**
    
    -   Ensure all Stripe API keys and Webhook Signing Secrets are stored securely, and never hard-code them in your source code.

----------

*Summary:*

By integrating Stripe with Teacup Tales, we provide a secure and user-friendly payment solution. This setup will handle all e-commerce transactions, improve the user experience, and offer flexibility in managing payment events and ensuring payment security.

### GMAIL 

Teacup Tales uses Gmail to manage email communications with users, including account verifications and purchase order confirmations. Integrating Gmail ensures reliable and secure delivery of transactional emails to enhance the customer experience.

#### **Steps for Gmail Integration:**

1.  **Create and Access Gmail Account:**
    
    -   Ensure you have an active Gmail (Google) account. Log in to your account.
2.  **Enable Two-Factor Authentication (2FA):**
    
    -   Go to your Google Account by clicking on your profile icon in the top-right corner and selecting "Manage Your Google Account."
    -   Navigate to the **Security** tab on the left sidebar.
    -   Under the "Signing in to Google" section, enable **2-Step Verification**. Follow the prompts to verify your password and activate 2FA.
3.  **Generate an App Password:**
    
    -   After enabling 2FA, stay on the **Security** page and select **App passwords**.
    -   Re-enter your password if prompted.
    -   Choose **Mail** as the app type and select **Other (Custom name)** for the device type. Enter a relevant name (e.g., "Teacup Tales Django App").
    -   Click **Generate** to create a 16-character app password (API key). **Note:** This password will only be displayed once, so save it securely.
4.  **Configure Email Settings in Your Application:**
    
    -   Update your application's email settings with the following credentials:
        -   **EMAIL_HOST_USER**: Your Gmail address (e.g., `your-email@gmail.com`)
        -   **EMAIL_HOST_PASSWORD**: The 16-character app password generated from Gmail.

#### **Security and Compliance:**

-   Ensure that your Gmail credentials, especially the app password, are stored securely and not hard-coded in your source code. Consider using environment variables or a secure secrets manager for this purpose.

----------

*Summary:*

By integrating Gmail, Teacup Tales can send secure and reliable emails for account verifications and purchase confirmations, enhancing communication with users and supporting overall customer engagement and satisfaction

### Deployment Process with Heroku

1.  Navigate to the [Heroku website](https://www.heroku.com/) and either [log in](https://id.heroku.com/login) to your existing account or [sign up](https://signup.heroku.com/) for a new account.
2.  From the dashboard, click the "New" button in the upper right corner and select "Create new App" from the drop-down menu.
3.  Provide a unique name for your application in the "App name" field.
    -   Heroku will indicate the name's availability with a green checkmark.
4.  Select the appropriate region ("United States" or "Europe") from the "Choose a region" dropdown, based on your target user base.
5.  Click the "Create app" button to proceed.
6.  On the next screen, navigate to the "Settings" tab located at the top center of the page.
7.  In the "Config Vars" section, click on the "Reveal config Vars" button to display the environment variable configuration interface.
8.  Input the necessary environment variables typically stored in your local `env.py` file. For this deployment, you will need to configure the following variables:
    -   **SECRET_KEY**: Django secret key.
    -   **AWS_ACCESS_KEY_ID**: Amazon AWS access key.
    -   **AWS_SECRET_ACCESS_KEY**: Amazon AWS secret access key.
    -   **AWS_STORAGE_BUCKET_NAME**: Name of your Amazon AWS S3 bucket.
    -   **EMAIL_HOST_PASS**: Password for your email service.
    -   **EMAIL_HOST_USER**: Email address used for outbound communications.
    -   **DATABASE_URL**: Link for database.
    -   **STRIPE_PUBLIC_KEY**: Stripe public key
    -   **STRIPE_SECRET_KEY**: Stripe secret key value
    -   **STRIPE_WH_SECRET**: Stripe wh value
    -   **USE_AWS**: True

9.  Enter each variable name in the "KEY" field and its corresponding value in the "VALUE" field.
10.  Return to the top of the page and select the "Deploy" tab.
11.  In the "Deployment method" section, choose "GitHub."
12.  Under "Connect to GitHub," click the "Search" button, locate your project repository, and click "Connect."
13.  Scroll down and click the "Deploy Branch" button to initiate the deployment.
14.  Consider enabling the automatic deployment option to allow Heroku to deploy your app automatically with each push to the GitHub repository.
15.  A build log will appear at the bottom of the screen. Upon successful deployment, a link to your application will be provided.

**Important!**: Ensure that your Heroku app URL is added to the `ALLOWED_HOSTS` setting in the `settings.py` file. Additionally, verify that the `DEBUG` setting is set to `False`, and the `requirements.txt` and `Procfile` are up to date and committed to GitHub.

[Back to top](#contents)

### To fork the project

Forking the **GitHub** repository allows you to create a duplicate of a local repository. This is done so that modifications to the copy can be performed without compromising the original repository.


- Log in to **GitHub**.

- Locate the repository.

- Click to open it.

- The fork button is located on the right side of the repository menu.

- To copy the repository to your **GitHub** account, click the button.

  
### To clone the project

- Log in to **GitHub**.

- Navigate to the main page of the repository and click **Code**.

- Copy the **URL** for the repository.

- Open your local **IDE**.

- Change the current working directory to the location where you want the cloned directory.

- Type git clone, and then paste the **URL** you copied earlier.

- Press **Enter** to create your local clone.
  

_Any changes required to the website, they can be made, committed and pushed to GitHub._

[Back to top](#contents)

## Testing

Teacup Tales Bookshop website underwent an extensive testing process to ensure its functionality, accessibility, and performance. This involved validating the code, assessing accessibility, conducting performance tests, performing cross-device testing, verifying browser compatibility, evaluating user stories, and incorporating user feedback to improve the overall user experience
Testing summary and results can be found in [TESTING.md](TESTING.md) file.

## Technology

###  Languages

- [Python](https://www.python.org/) 
- [Markdown](https://en.wikipedia.org/wiki/Markdown)
- [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML5 "HTML")
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS")
- [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript "JS")

### Frameworks

- [Django](https://www.djangoproject.com/): Django is the main Python framework used in the development of this project. It provides a robust and scalable architecture for building web applications.

### Python Libraries

- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Authentication library used to create user accounts, providing features such as registration, login, and social authentication.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): Used to manage Django forms, making form rendering in templates simpler and more elegant.
- [Humanize](https://pypi.org/project/humanize/): Used for turning a number into a fuzzy human-readable duration ("3 minutes ago")
- [Django-Summernote](https://pypi.org/project/django-summernote/): A library that integrates the Summernote WYSIWYG editor into Django forms, allowing for rich-text editing.
- [Django Countries](https://pypi.org/project/django-countries/): Library used to provide country choices for use with forms and a country field for models.
- [Pillow](https://pypi.org/project/Pillow/): Used to add image processing capabilities.  

### Programs

- [Balsamiq](https://balsamiq.com/): Wireframing tool used to generate wireframe images, allowing for quick and easy visualization of the application's layout and design.
- [Bootstrap](https://getbootstrap.com): CSS framework used for developing responsiveness and styling, offering a wide range of pre-designed components and utilities.
- [Google Chrome](https://developer.chrome.com/docs/devtools/): Used for overall development and tweaking, including testing responsiveness, debugging, and performance profiling.
- [Database Schema](https://dbdiagram.io/): database management tool used for creating and managing databases, providing features such as schema design, data modeling, and SQL querying.
- [Favicon](https://favicon.io/): Used to create the favicon, providing a simple tool for generating favicons for web applications.
- [Font Awesome](https://fontawesome.com/): Used for icons in the information bar, providing a wide range of high-quality, customizable icons for web development.
- [GitHub](https://github.com/): Used for version control and as an agile tool, facilitating collaborative development, code review, and project management.
- [Google Fonts](https://fonts.google.com/): Used to import and alter fonts on the page, offering a vast collection of free, open-source fonts for use in web projects.
- [Heroku](https://dashboard.heroku.com/login): Cloud-based platform used for deploying web applications. It offers easy deployment, scaling, and management of applications in the cloud environment.
- [Jshint](https://jshint.com/): Used to validate JavaScript code, helping identify potential errors and maintain code quality.
- [PEP8 Online](http://pep8online.com/): PEP8 Online is used to validate all Python code against the PEP 8 style guide, promoting code readability and consistency.
- [PostgreSQL](https://dbs.ci-dbs.net/): CI designed the database tool for this project. It is a powerful relational database management system.
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert Excel testing tables to Markdown format, simplifying the process of creating and formatting tables for documentation purposes.
- [TOC Generator](https://ecotrust-canada.github.io/markdown-toc/): Used to generate table of contents for Markdown files, providing a convenient way to organize and navigate large documents.
- [W3C](https://www.w3.org/): Used for HTML & CSS validation, ensuring that the project's code complies with web standards and is error-free.
- [WAVE](https://webaim.org/resources/contrastchecker/): Used for accessibility testing, providing tools to check for accessibility issues such as color contrast and semantic structure.
- [AWS](https://aws.amazon.com/) was used to store media files.
- [Stripe](https://stripe.com/en-ie) was integrated to handle payment processing in a secure and convenient way.

### Payment Service

   * [Stripe](https://stripe.com/en-gb-nl) was used to process all online payments transactions.


### Cloud Storage

* [Amazon Web Service S3](https://aws.amazon.com/s3/) was used to store all static and media files in production. 

[Back to top](#contents)

## Credits

- Feedback, advice and support:

  - [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin")

-  Listing content and visuals:

  - [Perplexity](https://www.perplexity.ai/)
  - [Leonardo.AI](https://leonardo.ai/)
  - [Amazon](https://www.amazon.com/)
  - [Coolors](https://coolors.co/)

- Learning content:

  - [CodePen](https://codepen.io/pen/)
  - [Automated Testing Tutorial](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)
  - [Django Documentation](https://docs.djangoproject.com/en/4.2/)
  - [Dev Community](https://dev.to/lindaojo/how-to-improve-lighthouse-score-accessibility-514e)
  - [Boostrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
  - [Dennis Ivy - Python Django 7 Hour Course](https://www.youtube.com/watch?v=PtQiiknWUcI)

- Debugging Issues:

  - [StackOverflow](https://stackoverflow.com/ "StackOverflow")
  - [Project Portfolio-4 channel on Slack](https://slack.com/intl/en-ie/ "Slack")
  - [Django Forum](https://forum.djangoproject.com/)


## Disclaimer

_Teacup Tales Bookshop provides free information only. It is not built for monetary profit. Every effort has been made to properly acknowledge and reference any images and information used in this project. Although the agreement for free usage allows photographs to be obtained by free search._

[Back to top](#contents)





