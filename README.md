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
