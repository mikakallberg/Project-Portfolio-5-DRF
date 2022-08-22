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
## Set up repository
#
- For the startup of this project the Django REST framework walkthrough was followed.
- Repository was set up in GitHub using the [Code Institute- gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template)
- The chosen name for the drf-API was Project-Porfolio-5-DRF, to have a consistent naming of all projects.
- When the repository was built, GitPod was chosen as the development platform.
- GitPod was allowed to build as the primary window to minimize the risk of anyhting getting lost in the build.
#
## Set up project in GitPod
#
- The following installments where made:
    - Install django by command: pip3 install 'django<4'
    - Install project by: django-admin startproject p5_api
    - Install Cloudinary-storage by: pip3 install django-cloudinary-storage
    - Install Pillow by: pip3 install Pillow
- Then create env.py-file to hide any sensitive information like cloudinary key and secret key.
- Set up settings.py exchanging the secret key for 'os.environ.get('SECRET_KEY')' and hiding the secret key in env.py,
  same with cloudinary key only this key needed to be set between curlybraces 'CLOUDINARY_URL':  os.environ.get('CLOUDINARY_URL') in the settings-file.
  Set up some os imports and host-settings.
- Create first app by: python3 manage.py startapp profiles
    - came across first bug.
- After model update the following commands where implemented in terminal:
   - python3 manage.py makemigrations --dry-run
   - python3 manage.py makemigrations
   - python3 manage.py migrate --plan
   - python3 manage.py migrate
   - pip3 freeze --local > requirements.txt (this command is also implemted every time a new dependency was installed)
- Installed apps (plus the ones listed above):
   - pip3 install djangorestframework
   - pip3 install dj-database-url (https://pypi.org/project/dj-database-url/)
   - pip3 install psycopg2 (https://pypi.org/project/psycopg2/)

#
* [Back to top](#)
#