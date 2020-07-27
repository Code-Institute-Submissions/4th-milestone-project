# 4th Milestone Project Code Institute

## Project purpose:

In this project, you'll build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

## Value provided:

- By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.
- The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

# Main Technologies

- HTML, CSS, JavaScript, Python+Django
- Relational database (recommending MySQL or Postgres)
- Stripe payments
- Additional libraries and APIs

# Mandatory Requirements

**Django Full Stack Project:**

- Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.

**Multiple Apps:**

- The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).

**Data Modeling:**

- Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course

**User Authentication:**

- The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).

**User Interaction:**

- Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).

**Use of Stripe:**

- At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.

**Structure and Navigation:**

- Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).

**Use of JavaScript:**

- The frontend should contain some JavaScript logic you have written to enhance the user experience.

**Documentation:**

- Write a README.md file for your project that explains what the project does and the value that it provides to its users.

**Version Control:**

- Use Git & GitHub for version control.

**Attribution:**

- Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.

**Deployment:**

- Deploy the final version of your code to a hosting platform such as Heroku.

**Security:**

- Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.

**This repo is for educational purposes only.**
