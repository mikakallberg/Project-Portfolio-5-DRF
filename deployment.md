# Social Media API
## Navigation
#
* [Deployed page]()
* [Learning Outcomes](/README.md#learning-outcomes)
* [Technologies and Libraries](/README.md#technologies-and-libraries)
* [Planning](/README.md#planning)
   - [Initial planning](/README.md#initial-plan)
   - [Plan](/README.md#plan)
   - [Lucid Chart](/README.md#lucidchart)
* [SetUp](/setup.md)
   - [Set up repository](/setup.md#set-up-repository)
   - [Set up project in GitPod](/setup.md#set-up-project-in-gitpod)
   - [Set up unique model in Gitpod](/setup.md#set-up-unique-model-in-gitpod)
* [User Experience](/README.md#user-experience-ux)
    - [Demographics](/README.md#demographics)
    - [User Goal](/README.md#user-goals)
* [Features](/features.md)
   - [Existing Features](/features.md#existing-features)
       - [Profile](/features.md#profile)
       - [Post](/features.md#post)
       - [Comments](/features.md#comments)
       - [Likes](/features.md#likes)
       - [Followers](/features.md#followers)
       - [Messages](/features.md#messages)
       - [Contacts](/features.md#contacts)
   - [New Features](/features.md#new-features)
* [Testing](/testing.md)
    - [First setup](/testing.md#first-setup)
    - [Testing in development](/testing.md#testing-in-development)
    - [Profile](/testing.md#profile)
    - [Post](/testing.md#post)
    - [Comments](/testing.md#comments)
    - [Likes](/testing.md#likes)
    - [Followers](/testing.md#followers)
    - [Messages](/testing.md#messages)
    - [Contacts](/testing.md#contacts)
* [Bugs](/bugs.md)
    - [Bugs in development](/bugs.md#bugs-in-development)
    - [Bugs left unsolved](/bugs.md#bugs-left-unsolved)
* [Deployment](/deployment.md)
    - [Initial Deployment](#initial-deployment)
    - [Final Deployment](#final-deployment)
* [Credits](/README.md#credits)
    - [Mentoring](/README.md#thank-you)
    - [Content credits](/README.md#content-credits)
    - [Media](/README.md#media)
#
## Initial Deployment
#
- After initial workspace setup in Gitpod and ensured launch in preview.
   - Followed the last walkthrough for clean up and deployment to Heroku.
    - Installed databases(Please view setup for more information):
        - psycopg2 and dj-database-url
        - django-cors-headers
        - Add Procfile with release versions makemigrations && migrate, and web(web gateway interface).
        - Add Heroku app to ALLOWED_HOSTS in settings.py
    - In Heroku:
       - Create app in Heroku
           - This was done according to previous plan, so app name was later changed.
           With changes being made in Gitpod workspace and Config vars in Heroku, to ensure functionality cross platforms.
       - Download Heroku Postgres-database
       - Ensure latest version pushed from Gitpod to Github.
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
       - This project will only collect cookies so that the user can log in automatically during a 24 hour window. It will not collect any statistics or any other information on the user.
       - A serializer-file was created in project app to serialize the cookie information.
    -Debug is set to a os.environ variable, so that when in production debug will be true, but not in production.
    - Allowed hosts are set to a os-environ variable to allow multiple outside projects to use this API.
    - Change Allowed hosts in Heroku config vars to match the name string used in settings.py.
    - A root_route page is created in the project app also a logout route, to enable users to logout properly.
    - Deploy page in Heroku successful.
    - Ensure that all apps with functions exists in the final deployed version as in development version.
        - exists in JSON-data
#
 Heroku contactlist                                                  | Heroku messagelist 
:------------------------------------------------------------------: | :---------------------------------------------------------------:
 ![Heroku contactlist](/assets/images_readme/heroku_contactlist.png) | ![Heroku messagelist](/assets/images_readme/heroku_messagelist.png)
#
* [Back to top](#)
#