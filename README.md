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


