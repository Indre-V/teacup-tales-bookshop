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

* Enhance User Experience:
 - Design a user-friendly interface that is intuitive, visually appealing, and easy to navigate.
 - Ensure the platform is fully responsive and accessible on all devices, including desktops, tablets, and smartphones.


* Facilitate Developer Showcase:
 - Enable registered users to create, edit, and manage posts and comments easily.
 - Introduce features that promote user engagement, such as the ability to like, favorite, and share content.


* Optimize Performance and Accessibility:
 - Fine-tune the platform for fast loading times and quick responses to user actions.
 - Adhere to accessibility standards to ensure an inclusive experience for all users.


* Support Continuous Improvement and Scalability:
 - Employ Agile development methodologies to deliver high-quality features and updates continuously.
 - Architect the database and infrastructure to efficiently handle increased traffic and user growth.

* Ensure Security and Reliability:
 - Implement strong authentication and authorization protocols to protect user data.
 - Conduct regular code validation and security testing to maintain a stable, secure application.
 
* Streamline Payment and Checkout:
 - Develop a smooth and secure payment process to enhance the checkout experience.
 - Provide multiple payment options and ensure compliance with payment security standards.

* Encourage Community Engagement and Feedback:
 - Create channels for users to provide feedback, report issues, and suggest enhancements.
 - Actively respond to user feedback and integrate improvements to continually refine the platform.

## Target Audience

 - Casual Shoppers
 - Book Enthusiasts
 - Independent Authors and Publishers
 - Accessibility-Focused Users

[Back to top](#contents)


## Wireframes

The wireframes for the platform provide a visual representation of the layout and structure of the application. They outline the placement of key elements such as navigation menus, user profiles, content areas, and interactive features. The wireframes ensure a cohesive and intuitive user interface, guiding the design and development process. After the extensive testing was conducted, naturally there are some deviations from wireframes in the live version of the platform.

[Wireframes](/docs/readme-md/wireframes.pdf "Wireframes")

[Back to top](#contents)
