# **_Naifat - Django REST Framework API_**

The repository you are viewing is for the back-end REST API and my front-end React project will be detailed underneath, [Naifat](https://drf-api-app-65d9b6a619df.herokuapp.com/).

You can view the live site here - <a href="https://drf-api-app-65d9b6a619df.herokuapp.com/" target="_blank" rel="noopener">Naifat</a>

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

# Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). The deployment process is as follows:

Firstly we need to create a new repository in [GitHub](https://github.com/) where our project files will be located

- Navigate to [GitHub](https://github.com/)
- Create a new repository.

Now it's time to install Django and some additional packages

- Install Django by typing **pip install 'django<4'**
- Create our new project by typing **django-admin startproject drf_api_deployment_process .**
- Install cloudinary storage by typing **pip install django-cloudinary-storage**
- Install Pillow by typing **pip install Pillow**

Now we need to add our newly installed apps to our **settings.py** file

Next, create a new **env.py** file and paste in the following code - remembering to change the "YOUR CLOUDINARY URL HERE" part to your API key

```Python
import os

os.environ["CLOUDINARY_URL"] = "YOUR CLOUDINARY_URL_HERE"

```

Back in our **settings.py** file we need to import our **env.py** file if it exists

```Python
import os

if os.path.exists("env.py"):
    import env
```

Now we need to reference our new Cloudinary URL in **settings.py**

```Python
CLOUDINARY_STORAGE = {"CLOUDINARY_URL": os.environ.get("CLOUDINARY_URL")}
```

Now we need to define our MEDIA_URL and DEFAULT_FILE_STORAGE in **settings.py**

```Python
MEDIA_URL = "/media/"

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
```

Now it's time to start creating our applications. For my project I created 6 seperate applications

- **drf_api**
- **comments**
- **followers**
- **likes**
- **posts**
- **profiles**

Don't forget to add these applications to the INSTALLED_APPS variable in **settings.py**

Next: 

Install JSON Web Token Authentication

- In the terminal type **pip install dj-rest-auth**

Add both rest framework’s auth token and django rest auth to INSTALLED APPS -

```Python
INSTALLED_APPS = [
    "rest_framework.authtoken",
    "dj_rest_auth",
]
```

Now add the urls to the urlpatterns list **path('dj-rest-auth/', include('dj_rest_auth.urls'))**

```Python
urlpatterns = [
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
]
```

Now migrate the database by typing **python manage.py migrate**

Next install Django All Auth with the following command - **pip install 'dj-rest-auth[with_social]'** and add the new application to the INSTALLED_APPS vairable in **settings.py**

```Python
INSTALLED_APPS = [
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
]
```

Now add a SITE_ID variable in **settings.py**

```Python
SITE_ID = 1
```

Add the registration urls to the urlpatterns list

```Python
urlpatterns = [
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
```

Now it's time to Add JWT tokens functionality, in the terminal type in the following command **pip install djangorestframework-simplejwt**

In **env.py** add the following variable

```Python
os.environ['DEV'] = '1'
```

In **settings.py** set the DEBUG value equal to the DEV variable you just set in **env.py**

```Python
DEBUG = 'DEV' in os.environ
```

Next, still in **settings.py** add the following code differentiate between development and production modes and also set the pagination and date time format

```Python
REST_PAGINATION = "rest_framework.pagination.PageNumberPagination"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        (
            "rest_framework.authentication.SessionAuthentication"
            if "DEV" in os.environ
            else "dj_rest_auth.jwt_auth.JWTCookieAuthentication"
        )
    ],
    "DEFAULT_PAGINATION_CLASS": REST_PAGINATION,
    "PAGE_SIZE": 100,
    "DATETIME_FORMAT": "%d %b %Y",
}
```

And now add the following code to **settings.py** to enable token authentication, cookie declaration and to also ensure that the tokens are sent over HTTPS only

```Python
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = "my-app-auth"
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"
JWT_AUTH_SAMESITE = "None"
```

Now we can create a new root route which will act as a welcome screen to anyone who visits the root route of our API

- Create a new **views.py** file in your main project folder (drf_api_league_hub) and add the following code

```Python
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    """
    Function to return a welcome message
    upon loading the API
    """
    return Response({"message": "Welcome to the League Hub DRF API!"})
```

Add that new route to the urlpatterns list in the main **urls.py** file

```Python
from .views import root_route

    path("", root_route),
```

Create a new production database with [ElephantSQL](https://www.elephantsql.com/)

- Log into [ElephantSQL](https://www.elephantsql.com/)
- Click **Create New Instance**
- Give your plan a name
- Select \*_Tiny Turtle (Free)_ plan
- Click **Select Region** and pick a data center near you
- Click **Review**, double check the information you provided, once happy, click **Create Instance**

We need to get the new database URL from the [ElephantSQL](https://www.elephantsql.com/) dashboard.

Return to the dashboard, find your newly created plan and copy the URL

Back in our local project, in **eny.py** we can add our copied production database URL and store it in a new variable which can be referenced without exposing the value to unwanted eyes

```Python
os.environ.setdefault(
    "DATABASE_URL", "YOUR DB URL HERE",
)
```

In the terminal, type in **pip install dj_database_url**

After that has installed, we need to import it into our main **settings.py** file

```Python
import dj_database_url
```

Now we can seperate the development and production environment databases with the following code

```Python
if "DEV" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {"default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"))}
    print("Connected to live database")
```

Next we need to install gunicorn. In the terminal, type in the following

- **pip install gunicorn**

Now created a Procfile at the root level in your project


Within that newly created Procfile, add the following code to let Heroku know how to run the project

```Python
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api_league_hub.wsgi
```

Back in **settings.py**, we need to tell the project which hosts to allow

```Python
ALLOWED_HOSTS = [
    os.environ.get("ALLOWED_HOST"),
    "127.0.0.1",
]
```

Now it's time to install **CORS**

In the terminal, **pip install django-cors-headers** and then add to the INSTALLED_APPS

```Python
INSTALLED_APPS = [
    'corsheaders',
]
```

Add it to the MIDDLEWARE list at the top of the list

```Python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
]
```

Now we need to set the ALLOWED_ORIGINS for the network requests made to the server. In **settings.py** file, add the below

```Python
if "CLIENT_ORIGIN" in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get("CLIENT_ORIGIN"),
    ]
if "CLIENT_ORIGIN_DEV" in os.environ:
    CORS_ALLOWED_ORIGINS.append(os.environ.get("CLIENT_ORIGIN_DEV"))

CORS_ALLOW_CREDENTIALS = True

JWT_AUTH_SAMESITE = 'None'
```

Now we need to replace the SECRET_KEY variable in **settings.py** to reference the secret key that we will create in **env.py**

In **env.py** create a new variable called SECRET_KEY and give it a value

```Python
os.environ.setdefault("SECRET_KEY", "YOUR SECRET KEY HERE")
```

Now back in **settings.py**, change the SECRET_KEY value to point to the SECRET_KEY you just created in **env.py**

```Python
SECRET_KEY = os.getenv("SECRET_KEY")
```

Update the requirements file by typing in the command in the terminal **pip freeze > requirements.txt**

- git add
- git commit -m "{message here}
- git push

Now it's time to deploy our new project live for everyone to see on [Heroku](https://www.heroku.com)

- Navigate to [Heroku](https://www.heroku.com)
- Click **New app**
- Fill in the relevant information
- Click **Create app** once you are happy


Once you've created your new [Heroku](https://www.heroku.com) application, we need to add some config variables. Click the **settings** tab and then click **Reveal Config Vars**

Make sure to add the following config variables

- ALLOWED_HOST - This is the URL of your deployed project (without the https)
- CLIENT_ORIGIN - This is the URL of your deployed front-end project
- CLIENT_ORIGIN_DEV - This is the URL when developing locally
- CLOUDINARY_URL - This is your Cloudinary API key
- DATABASE_URL - This is your production database URL
- DISABLE_COLLECTSTATIC - This will be removed before submission
- SECRET_KEY - This is the secret key you have created


Now we need to link our [Heroku](https://www.heroku.com) application with our [GitHub](https://github.com/) project

- Click the **Deploy** tab
- Choose **GitHub**
- Search for your repository
- Once found, click **Connect**

Finally, we can deploy our connected projected for everyone to see.

You can either choose **Enable Automatic Deploys** or **Deploy Branch**. I chose to deploy my application automatically.

- Click **Deploy Branch** and wait for it to build

[Back to top](#contents)

### Content

This project was created and inspired by following the [Code Institute](https://codeinstitute.net/) DRF-API walkthrough.

I spent some time looking through the official [Django REST Framework Documentation](https://www.django-rest-framework.org/api-guide/permissions/) to also aid my development.

[Back to top](#contents)

# **_Naifat_**

This part of the repository you are viewing is for the front-end of the app [Naifat](https://drf-api-app-65d9b6a619df.herokuapp.com/).

You can view the live site here - <a href="https://drf-api-app-65d9b6a619df.herokuapp.com/" target="_blank" rel="noopener">Naifat</a>.

![Naifat responsive design](../drf-api/images/frontendimgs/amires.png)

# Contents

- [**Objective**](#objective)
- [**User Experience UX**](#user-experience-ux)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
  - [Design Prototype](#design-prototype)
  - [Design Choices](#design-choices)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Project Management](#project-management)
- [**Permissions**](#permissions)
  - [Logged Out User](#logged-out-user)
  - [Logged In User](#logged-in-user)
- [**Existing Features**](#existing-features)
  - [Home Page](#home-page)
  - [Responsive Navigation Bar](#responsive-navigation-bar)
  - [Search Bar](#search-bar)
  - [Sign In Page](#sign-in-page)
  - [Sign Up Page](#sign-up-page)
  - [Profile Page](#profile-page)
  - [Signed In Home Page](#signed-in-home-page)
  - [Create Post](#create-post)
  - [Edit Post](#edit-post)
  - [Comments](#comments)
  - [Popular Reviewers](#popular-reviewers)
- [**Future Features**](#future-features)
  - [Events](#events)
  - [News](#news)
  - [Streams](#streams)
- [**Technologies Used**](#technologies-used)
- [**Testing**](#testing)
- [**Deployment To Heroku**](#deployment-to-heroku)
- [**Credits**](#credits)
  - [**Content**](#content)
  - [**Media**](#media)
- [**Acknowledgments**](#acknowledgements)

# Objective

For my fifth and final project, I intend to create an online blog still social platform where many beauty enthusiasts can come together to share their knowledge and passion on all things, bath, beauty and glamour. I aim to demonstrate a good understanding in creating a website using React JS for the front end and Django REST framework for the backend whilst adhering to agile methodologies.

[Back to top](#contents)

## Project Goals

1 - Build a project to help users gain knowledge on different beauty products <br>
2 - Ensure the project is fully responsive to cater for all user device screen sizes <br>
3 - Design an intuitive layout that promotes a positive user experience <br>
4 - Implement a theme that compliments the project <br>
5 - Allow users to quickly search for a post <br>
6 - Allow users to filter posts <br>
7 - Give the users the ability to edit and remove a post <br>
8 - Give the users the ability to view who the 'popular reviewers' are <br>
9 - Give the users the ability to create/edit and delete a comment on a post <br>
10 - Require users to have an account to access additional features <br>

## User Stories

My user stories are in the project of my respository where I worked on the front end of my app before combining my workspaces.

You can view this project from *<a href="https://github.com/NaifatSelina/naifat" target="_blank" rel="noopener">this</a>* repository.

![User Stories](../drf-api/images/frontendimgs/user%20stories%201.png)
![User Stories](../drf-api/images/frontendimgs/user%20stories%202.png)

[Back to top](#contents)

## Design Prototype

During the design wireframes process I decided to use [Figma](https://www.figma.com/) in my project. Figma quickly and efficiently allows me to create outlines for how I would like my project to look. I was able to create a rough colour scheme that I knew I wanted to use, something clean, fresh and timeless. The simplistic layout and structure of each of the design wireframes is something which I wanted to keep in the final version of the app as I knew I needed the beauty app to be easy to navigate to heighten accessability. My audience for this app was people of all technical capabilities, as everyone should be able to come together to learn and share their knowledge and learn about the beauty services and products they are indulging in- it was a necessity that the structure remained simple.

<br>
<br>
<br>

![Figma Design](../drf-api/images/frontendimgs/CreatePostWF.png)

![Figma Design](../drf-api/images/frontendimgs/HomePageWF.png)

![Figma Design](../drf-api/images/frontendimgs/ProfilePageWF.png)

![Figma Design](../drf-api/images/frontendimgs/SignedInHomePageWF.png)

![Figma Design](../drf-api/images/frontendimgs/SignInWF.png)

![Figma Design](../drf-api/images/frontendimgs/SignUpWF.png)

<br />

[Back to top](#contents)




# Naifat 2023.



