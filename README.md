# 4th-milestone-project

Codejob.ie is a Full Stack web application, part of my Full Stack Developer study at Code Institute, that allows job seekers to search for (remote) jobs and recruiters to advertise their jobs. Searching for jobs is at no costs, though recruiters are obliged to pay a monthly fee to be able to publish their job profiles. At all time recruiters can cancel their membership.

A live demo can be found [here](https://codejob.herokuapp.com/).

## Project purpose:
Build a full-stack site based around business logic used to control a centrally-owned dataset. Set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

## Value provided:
- By authenticating on the site and paying for some of its services, users can advance their own goals. Before authenticating, the site makes it clear how those goals would be furthered by the site.
- The site owner is able to make money by providing this set of services to the users. There is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.

Further requirements can be found [here](https://github.com/GitNorthWay/4th-milestone-project/tree/develop/documentation/assignment).

#UX
While creating this web application I had user stories in mind, have chosen colors and typography wisely and made a wireframe.
## User stories
For an optimal user experiences I made user stories. I also prioritized them using the MoSCoW method. 

You can download the user stories [here](https://github.com/GitNorthWay/4th-milestone-project/blob/develop/documentation/assignment/user_stories_codejob.xlsx).

## Colors
In the web application there are two main colors; blue and green. Blue is often associated with depth and stability. It symbolizes trust, loyalty, wisdom and confidence. These are typically characteristics which symbolize software engineers. Green stands for growth and health. It is also seen as a refreshing and peaceful color. The association of growth matches perfectly with the goal of a job portal.
The main colors used in the site are:
![#007bff](https://placehold.it/15/007bff /007bff) `#007bff`
![#6c757d](https://placehold.it/15/6c757d/6c757d) `#6c757d`
![# 28a745](https://placehold.it/15/28a745/28a745) `#28a745`
![#17a2b8](https://placehold.it/15/17a2b8/17a2b8) `#17a2b8`
![#ffc107](https://placehold.it/15/ffc107/ffc107) `#ffc107`
![#dc3545](https://placehold.it/15/dc3545/dc3545) `#dc3545`
![#f8f9fa](https://placehold.it/15/f8f9fa/f8f9fa) `#f8f9fa `
![#343a40](https://placehold.it/15/343a40/343a40) `#343a40`

## Features
I have added the following features to the web application:
-	View a list of jobs
-	Search jobs
-	Easily register for an account
-	Easily login and logout
-	Have a personalized profile (recruiters and candidates)
-	Editing personalized profile (recruiters and candidates)
-	Pay monthly fee to activate recruiter profile

## Features left to implement
-	Add jobs to favorite
-	Recover password
-	Receive email after registration
-	Have a personalized candidate profile publicly (recruiters and candidates)
-	Add jobs or companies to favorites
-	Messaging system between candidates and recruiters
-	View history of payments

# Technologies used

## Tools
-	Virtual Studio Code as IDE for coding
-	GitHub for version control
-	ExtendsClass for validating Python
-	Markup Validation Service for validating HTML
-	CSS Validation Service for validating CSS
-	JSHint for validating jQuery
-	Favicon generator

## Frontend technologies
-	HTML
-	CSS
-	Bootstrap 4.5.0
-	Font Awesome 4.7.0
-	jQuery 3.5.1
- JavaScript

## Backend technologies
The main backend technologies are:
-	Python as coding language
-	Django as web framework for rapid development
-	Stripe as secure payment platform
-	AWS S3 to store uploaded images
-	Boto3 as the Python SDK for AWS S3
-	Crispy Forms to style forms
-	Django Heroku for deployment on Heroku
-	Django Storages as storage backend to work with Boto3 and AWS S3
-	Pillow as Python Image Library
-	Heroku as hosting the web application

## Databases
-	SQlite3 as development database
-	PostgreSQL for production database on Heroku

You can find the database model [here](https://github.com/GitNorthWay/4th-milestone-project/blob/develop/documentation/assignment/database_model_codejob.xlsx).

# Deployment
Deployment
-	Clone the project in the folder of your choice on your computer. Use the command in Git Bash or your IDE:
```git clone https://github.com/GitNorthWay/4th-milestone-project.git```
-	Install Heroku CLI if you haven’t installed it yet:
```https://devcenter.heroku.com/articles/heroku-cli```
-	Create an account at Heroku of you haven’t already one:
```https://www.heroku.com/```
-	Login at Heroku, preferably via your IDE with the command:
```heroku login```
-	Create an app with the command:
```heroku create <nameapp>```
-	Check if app was created successfully:
```heroku open```
-	Add PostgeSQL database (free version) with the command:
```heroku addons:create heroku-postgresql:hobby-dev```
-	Push code to Heroku with the command:
```git push heroku master```
-	Run migrations with the command:
```heroku run python manage.py migrate```
-	Create super user to be able to access Django admin
```heroku run python manage.py createsuperuser```
-	Create an account at Stripe and login:
```https://www.stripe.com```
-	Add new product
```https://dashboard.stripe.com/test/products```
-	Add two price plans:
```Jobseekerplan (0 per month) and Recruiterplan (25 per month)```
-	Add API-ID’s of both plans in Django admin under Plans
- You have successfully deployed this project to Heroku


# Credits & acknowledgements

## Images
- [default profile image](https://pixabay.com/nl/vectors/man-business-cartoon-zakenman-1352025) from image owner [ROverhate](https://pixabay.com/nl/users/roverhate-1759589/)
- [testimonial image 1](https://pixabay.com/nl/photos/baard-gezicht-man-model-snor-1845166/) from image owner [Pexels](https://pixabay.com/nl/users/pexels-2286921/)
- [testimonial image 2](https://pixabay.com/nl/photos/meisje-lachend-vrouwelijke-vrouw-872149/) from image owner [Free-Photos](https://pixabay.com/nl/users/free-photos-242387/)
- [homepage banner](https://pixabay.com/nl/photos/man-laptop-het-werk-digitale-nomade-4749237) from image owner [Peggy_Marco](https://pixabay.com/nl/users/peggy_marco-1553824/)

## Coding tips & tricks
- [Abstract user](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
- [Django Decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)
- [Pagination](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)
- [Collectstatic error on Heroku)(https://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku)

# Most used languages and frameworks
- [Most spoken languages](https://www.babbel.com/en/magazine/the-10-most-spoken-languages-in-the-world)
- [Most popular coding languages](https://www.businessinsider.nl/most-popular-programming-languages-github-2019-11)
- [Top web development frameworks](ttps://www.appypie.com/top-web-development-frameworks)



**This repo is for educational purposes only.**
