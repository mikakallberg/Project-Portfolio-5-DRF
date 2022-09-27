# Name pending

## Navigation Through Content
#
* [Deployed page]()
* [Project Purpose](#project-purpose)
    - [Learning Outcomes](#learning-outcomes)
    - [Project Requirements](#project-requirements)
* [Initial Planning](/deployment.md)
* [Initial SetUp](/setup.md)
    - [Set up repository](#set-up-repository)
    - [Set up project in GitPod](#set-up-project-in-gitpod)
    - [Set up....]()
* [User Experience](#user-experience-ux)
    - [Demographics](#demographics)
    - [User Goal](#user-goals)
* [Features](/features.md)
   - [Existing features](/features.md#existing-features)
   - [Possible improvements](/features.md#features-left-to-implement)
* [Testing](/testing.md)
    - [Validator Testing](/testing.md#validator-testing)
    - [Manual testing](/testing.md#manual-testing)
    - [Automated Testing](/testing.md#automated-testing)
* [Bugs](/bugs.md)
* [Deployment](/deployment.md)
* [Credits](#credits)
    - [Mentoring](#mentoring)
    - [Content credits](#content-credits)
    - [Media](/credits.md)
      -[Blog Content credits](/credits.md#blog-content-credits)
        - [Why Soil Matters](/credits.md#why-soil-matters)
        - [How to grow tomatoes](/credits.md#how-to-grow-tomatoes)
        - [How to grow carrots](/credits.md#how-to-grow-carrots)
        - [The humble potatoe](/credits.md#the-humble-potatoe)
        - [The frail but worth it salad](/credits.md#the-frail-but-worth-it-salad)
        - [The hearty onion](/credits.md#the-hearty-onion)
        - [The plump Bell Pepper](/credits.md#the-plump-bell-pepper)
     - [Image Credits](/credits.md#image-credits)
        - [About us picture](/credits.md#about-us-picture)
        - [Favicons](/credits.md#favicons)
        - [Creation Credits](/credits.md#creation-credits)
#
## Initial Deployment
#
- After initial workspace setup in Gitpod and ensured launch in preview.
   - Followed the last walkthrough for clean up and deployment to Heroku.
    - Installed databases(Please view setup for more information):
        - psycopg2 and dj-database-url
        - django-cors-headers
    - In Heroku:
       - Create app in Heroku
           - This was done according to previous plan, so app name was later changed.
           With changes being made in Gitpod workspace and Config vars in Heroku, to ensure functionality cross platforms.
       - Download Heroku Postgres-database
       - Ensure latest version pushedfrom Gitpod to Github.
       -Connect App in Heroku to workspace in Github.
       - Config vars
           - ALLOWED_HOSTS
           - CLIENT_ORIGIN_DEV
           - CLOUDINARY_URL
           - DATABASE_URL
           - DISABLE_COLLECT_STATIC
           - SECRET_KEY
        - After all steps where compaired with launch instrcutions in walkthrough first manual deployment was attempted, with bug. 
           - For bug story please read [Bugs in development](/bugs.md)


#
Launch Successful in preview                         | Profiles succesfull
:--------------------------------------------------: | :--------------------------------------------------:
 ![Launch](/assets/images_readme/launch_success.jpeg)| ![Profiles test](/assets/images_readme/first_profile_test.jpeg)
#
Successfull launch in Heroku                        |
:--------------------------------------------------:|
  ![Herokku launch](/assets/images_readme/heroku_success_test.jpeg)
#
## Final Deployment
#
- Following the walkthrough on deployment.
    - Redownloading all the applications.
    - Download:
       - [Corsheaders](https://pypi.org/project/django-cors-headers/)
       - [DJ-REST-AUTH](https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)
       - [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
    - Enable crossorigin communication between the current back end and future front end apps, with settings in settings.py:
        - JWT_AUTH_SAMESITE
        - if-statements for CLIENT_ORIGIN_DEV, for using different urls in deployment and production.
    - CORS_ALLOWED_CREDENTIALS, to enable cookie authetication so the User is able to automatically be logged from the same source within a 24 hour window.
    - JW-tokens for cookies and secure https-url connection. 
       - This project will only collect cookies so that the user can log in automatically during a 24 hour window. It will not collect any stattistics or any other information the user.
       - A serializer-file was created in project app to serialize the cookie information.
    -Debug is to a os.environ variable, so that when in production debug will be true, but not in production.
    - Allowed hosts are set to a os-environ variable to allow multiple outside projects to use this API.
    - A root_route page is created in the project app also a logout route, to enable users to logout properly.
    -

#
* [Back to top](#)
#