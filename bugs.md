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
## Bugs left unsolved
#
- In settings.py the following bugs is left unsolved:
   - 're' imported but unused
      - It is not being unused [Python doc on re](https://docs.python.org/3/library/re.html).
   -'env' imported but unused
      - The env is in an if statement and is therefore under conditional use. In localhost as in preview the env-file is implemented,
        where as in Heroku cofig vars are used.
   - 4 line to long on line 102, 105, 108 and 111. 
      - These can't be modified, since doing so will create a more serious error that affects functionality.

#
* [Back to top](#)
#