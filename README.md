# **_Naifat - Django REST Framework API_**

The repository you are viewing is for the back-end REST API used for my front-end React project, [naifat](https://naifat-75fb49666f3a.herokuapp.com/).

You can view the live site here - <a href="https://naifat-75fb49666f3a.herokuapp.com/" target="_blank" rel="noopener">Naifat</a>

You can view the live API here - <a href="https://drf-api-app-65d9b6a619df.herokuapp.com/" target="_blank" rel="noopener">Naifat DRF API</a>

You can view the front-end README.md here - <a href="https://github.com/NaifatSelina/naifat" target="_blank" rel="noopener">Naifat Front-End README</a>

You can view the back-end README.md here - <a href="https://github.com/NaifatSelina/drf-api" target="_blank" rel="noopener">Naifat Back-End README</a>

# Contents

- [**Objective**](#objective)
- [**Database**](#database)
- [**Models**](#models)
- [**Testing**](#testing)
  - [**Manual Testing**](#manual-testing)
  - [**PEP8 Validation**](#pep8-validation)
  - [**Bugs Fixed**](#bugs-fixed)
  - [**Bugs Unresolved**](#bugs-unresolved)
- [**Technologies Used**](#technologies-used)
- [**Deployment To Heroku**](#deployment-to-heroku)
- [**Cloning This Project**](#cloning-and-setting-up-this-project)
- [**Credits**](#credits)
  - [**Content**](#content)
  - [**Media**](#media)

# Objective

The main aim of the Djange Rest Framework API is to provide a reliable and secure way for the data used in my [naifat](https://naifat-75fb49666f3a.herokuapp.com/) front-end project to be provided. The aim of this API is to be simple and efficient so the data required for the application can be represented well.

[Back to top](#contents)

# Database

For this project, I implemented a PostgreSQL database hosted by [ElephantSQL](https://www.elephantsql.com/) for the production database.

![PostgreSQL](images/postgresql.png)

[Back to top](#contents)

# Models

### Followers

The followers model is designed to contain all relevent information regarding what followers users on the Naifat platform have.

![followersmodel](images/followers%20model.png)


### Likes
The likes model is designed to contain all relevent information regarding what likes posts on the Naifat platform have.

![likesmodel](images/likes%20model.png)

### Posts
The posts model is designed to contain all relevent information regarding what posts users on the Naifat platform are creating.

![postsmodel](images/posts%20model.png)

### Profiles 
The profiles model is designed to contain all relevent information regarding what users are being created on the Naifat platform.

![profilesmodel](images/profiles%20model.png)

### Comments
The comments model is designed to contain all relevent information regarding what comments users on the Naifat platform are leaving under posts.

![commentsmodel](images/comments%20model.png)

[Back to top](#contents)

# Testing

- ## Manual Testing

![manualtest](images/manualtests.png)

- ## PEP8 Validation

  I've tested all the files through the [CI PEP8 Linter](https://pep8ci.herokuapp.com/#) and although I found a few errors, I have rectified these and now all files are passing with "All clear, no errors found", as for the settings file for my drf_api application, the errors relating to the lines being too long only refer to long paths that must be on one line.

  ### drf_api

  ![drf_pep1](images/permissions.py.png)
  ![drf_pep2](images/manage.py.png)
  ![drf_pep3](images/serializer.py.png)
  ![drf_pep4](images/settings.py%20.png)
  ![drf_pep5](images/urls.py.png)

  ### comments

  ![drf_pep6](images/commentmodels.py.png)
  ![drf_pep7](images/commentserializers.py.png)
  ![drf_pep8](images/commenturl.py.png)
  ![drf_pep9](images/commentviews.py.png)

  ### followers
  ![drf_pep10](images/followersserializers.py.png)
  ![drf_pep11](images/followersmodels.py.png)
  ![drf_pep12](images/followersurls.py.png)
  ![drf_pep13](images/followersviews.py.png)

  ### likes 
  ![drf_pep14](images/likesserializers.py.png)
  ![drf_pep15](images/likesmodels.py.png)
  ![drf_pep16](images/likesurls.py.png)
  ![drf_pep17](images/likesviews.py.png)

  ### posts
  ![drf_pep18](images/postsmodels.py.png)
  ![drf_pep19](images/postsserializers.py.png)
  ![drf_pep20](images/poststests.py.png)
  ![drf_pep21](images/postsurls.py.png)
  ![drf_pep22](images/postsviews.py.png)

  ### profiles
  ![drf_pep23](images/profilesmodels.py.png)
  ![drf_pep24](images/profilesserializers.py.png)
  ![drf_pep25](images/profilesurls.py.png)
  ![drf_pep26](images/profilesviews.py.png)

- ## Bugs Fixed

#### Through my development I encountered some easily fixed bugs, firstly my workspace was throwing an error due to my mistake of putting CLOUDINARYURL before my cloudinary link in my env.py file, I removed this and the eroor was gone.
 ![bugs1](images/error.png)
 ![bugs2](images/error%202.png)


#### This error occurred due to my settings.py file not included the up to date version of my gitpod url for the workspace- this was fixed by updating the url.
 ![bugs3](images/deployment%20error.png)


 #### In this error I forgot to add a capital P to my Procfile- this was easily fixed.
 ![bugs4](images/procfileerror.png)

 - ## Bugs Unresolved

  - As far as I'm aware, there are not any unresolved bugs<br />

  # Technologies Used

## Languages

- [Python](https://www.python.org/) - A programming language that lets you work quickly
  and integrate systems more effectively

## Libraries and Frameworks

- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [Django REST Framework](https://pypi.org/project/djangorestframework/) - A powerful and flexible toolkit for building Web APIs

# Technologies Used

## Languages

- [Python](https://www.python.org/) - A programming language that lets you work quickly
  and integrate systems more effectively

## Libraries and Frameworks

- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [Django REST Framework](https://pypi.org/project/djangorestframework/) - A powerful and flexible toolkit for building Web APIs

## Packages


- [cloudinary](https://pypi.org/project/cloudinary/) - Easily integrate your application with Cloudinary
- [dj-database-url](https://pypi.org/project/dj-database-url/) - Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - API endpoints for handling authentication securely in Django Rest Framework
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - package that facilitates integration with Cloudinary by implementing Django Storage API
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Adds Cross-Origin Resource Sharing (CORS) headers to responses.
- [django-extensions](https://pypi.org/project/django-extensions/) - Collection of global custom management extensions for the Django Framework.
- [django-filter](https://pypi.org/project/django-filter/) - Declaratively add dynamic QuerySet filtering from URL parameters.
- [django-rest-auth](https://pypi.org/project/django-rest-auth/) - Provides a set of REST API endpoints for Authentication and Registration
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - A Python WSGI HTTP Server for UNIX.
- [oauthlib](https://pypi.org/project/oauthlib/) - Implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [pathspec](https://pypi.org/project/pathspec/) - Utility library for pattern matching of file paths
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python
- [PyJWT](https://pypi.org/project/PyJWT/) - Library for encoding and decoding JSON Web Tokens (JWT)
- [requests](https://pypi.org/project/requests/) - Allows you to send HTTP/1.1 requests
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib authentication support for Requests
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python.

## Other Tools

- [Gitpod](https://www.gitpod.io/) - Used to create and edit the website.
- [GitHub](https://github.com/) - Used to host and deploy the website as well as manage the project.
- [GitBash](<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>) - Terminal used to push changes to the GitHub repository.
- [Heroku](https://dashboard.heroku.com) - Used to deploy the website
- [ElephantSQL](https://www.elephantsql.com/) - Provides a browser tool for SQL queries where you can create, read, update and delete data directly from your web browser.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files .
- [TablePlus](https://tableplus.com/) - Used to view databases in a clean, simple way.
- [CI PEP8 Linter](https://pep8ci.herokuapp.com/#) - Used to check the Python code for any linting issues

[Back to top](#contents)


