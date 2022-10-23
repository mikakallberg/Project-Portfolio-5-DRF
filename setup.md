# Social Media API

![Am I Responsive]()
## Navigation Through Content
#
* [Deployed page]()
* [Learning Outcomes](/README.md#learning-outcomes)
* [Technologies and Libraries](/README.md#technologies-and-libraries)
* [Planning](/README.md#planning)
   - [Initial planning](/README.md#initial-plan)
   - [Plan](/README.md#plan)
   - [Lucid Chart](/README.md#lucidchart)
* [Initial SetUp](/setup.md)
   - [Set up repository](#set-up-repository)
   - [Set up project in GitPod](#set-up-project-in-gitpod)
   - [Set up unique model in Gitpod](#set-up-unique-model-in-gitpod)
* [User Experience](/README.md#user-experience-ux)
    - [Demographics](/README.md#demographics)
    - [User Goal](/README.md#user-goals)
* [Features](/features.md)
   - [Existing features](/features.md#existing-features)
   - [Possible improvements](/features.md#features-left-to-implement)
* [Testing](/testing.md)
    - [Validator Testing](/testing.md#validator-testing)
    - [Manual testing](/testing.md#manual-testing)
    - [Automated Testing](/testing.md#automated-testing)
* [Bugs](/bugs.md)
* [Deployment](/deployment.md)
* [Credits](/README.md#credits)
    - [Mentoring](/README.md#thank-you)
    - [Content credits](/README.md#content-credits)
    - [Media](/README.md#media) 
#
## Set up repository
#
- For the startup of this project the Django REST framework walkthrough was followed.
- Repository was set up in GitHub using the [Code Institute- gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template)
- The chosen name for the project was Project-Porfolio-5-DRF, to have a consistent naming of all projects.
- When the repository was built, GitPod was chosen as the development platform.
- GitPod was allowed to build as the primary window to minimize the risk of anyhting getting lost in the build.
#
## Set up project in GitPod
#
- The following installments where made:
    - Install django by command: [pip3 install 'django<4'](https://www.djangoproject.com/)
    - Install project by: django-admin startproject p5_api
    - Install Cloudinary-storage by: [pip3 install django-cloudinary-storage](https://cloudinary.com/documentation/django_integration)
    - Install Pillow by: [pip3 install Pillow](https://pillow.readthedocs.io/en/stable/)
- Then create env.py-file to hide any sensitive information like cloudinary key and secret key.
- Set up settings.py exchanging the secret key for 'os.environ.get('SECRET_KEY')' and hiding the secret key in env.py,
  same with cloudinary key only this key needed to be set between curlybraces 'CLOUDINARY_URL':  os.environ.get('CLOUDINARY_URL') in the settings-file.
  Set up some os imports and host-settings.
- Create first app by: python3 manage.py startapp profiles
    - came across first bug.
    -subseqent apps created by command python3 manage.py startapp "app name"
- After model update the following commands where implemented in terminal:
   - python3 manage.py makemigrations --dry-run
   - python3 manage.py makemigrations
   - python3 manage.py migrate --plan
   - python3 manage.py migrate
   - pip3 freeze --local > requirements.txt (this command is also implemted every time a new dependency was installed)
- Installed apps (plus the ones listed above):
   - [pip3 install djangorestframework](https://www.django-rest-framework.org/)
   - [pip3 install dj-database-url](https://pypi.org/project/dj-database-url/)
   - [pip3 install psycopg2](https://pypi.org/project/psycopg2/)
   - [pip3 install django-filter](https://django-filter.readthedocs.io/en/stable/)
   - [pip3 install dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
   - [pip3 install 'dj-rest-auth[with_social]'](https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional)
#
## Set up unique model in Gitpod
#
- Install Channels with Daphne ASGI
   - Consulted both docs and mentor to make sure I dont have any third party apps that will clash with Chanelles or Daphne, since this app will take over the terminal.
   - python3 -m pip3 install -U channels["daphne"]
   - Add channels and daphne to p5_api/settings.py/INSTALLED_APPS according to instructions in Channel [documentation](https://channels.readthedocs.io/en/latest/index.html)
   - Follwed instructions in the video I have taken inpsiration from [Code With Stein](https://www.youtube.com/watch?v=SF1k_Twr9cg)
   - Changed code according to my class-based project, video from Youtube shows groupchats, my chat is contact-based.
   - App imessages inhabits the chat, the app contacts has potential to become a groupchat.

#
* [Back to top](#)
#