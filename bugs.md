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
## Bugs in development
#
- At first the workspace couldn't create the profile app error-message "can't open file 'manage.py': [Errno 2] No such file or directory".
   - File existed
   - File was located inside a p5_api folder, when the project folder ws created it created double folders, put the manage.py-file inside the first folder next to
     the second p5_api-folder that contained all the python files for the project.
   - Solution: Move all files outside both folders, delete the inner p5_api-folder, move all python-files but the manage.py file inside the one remaining p5_api folder. Create app.
   - App successfully created.
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

#
* [Back to top](#)
#