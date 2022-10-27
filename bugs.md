# Social Media API
* [Deployed Front-End page](https://cozycorner-pp5.herokuapp.com/)
* [Deployed Back-End page](https://portfolio-project-5-drf-api.herokuapp.com/)
#
## Navigation
#
* [Bugs](/bugs.md)
   - [Bugs in development](#bugs-in-development)
   - [Bugs left unsolved](#bugs-left-unsolved)
* [Credits](/README.md#credits)
    - [Mentoring](/README.md#thank-you)
    - [Content credits](/README.md#content-credits)
    - [Media](/README.md#media)
* [Deployment](/deployment.md)
   - [Initial Deployment](/deployment.md#initial-deployment)
   - [Final Deployment](/deployment.md#final-deployment)
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
* [Learning Outcomes](/README.md#learning-outcomes)
* [Planning](/README.md#planning)
   - [Initial planning](/README.md#initial-plan)
   - [Plan](/README.md#plan)
   - [Lucid Chart](/README.md#lucidchart)
* [SetUp](/setup.md)
   - [Set up repository](/setup.md#set-up-repository)
   - [Set up project in GitPod](/setup.md#set-up-project-in-gitpod)
   - [Set up unique model in Gitpod](/setup.md#set-up-unique-model-in-gitpod)
* [Technologies and Libraries](/README.md#technologies-and-libraries)
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
* [User Experience](/README.md#user-experience-ux)
    - [Demographics](/README.md#demographics)
    - [User Goal](/README.md#user-goals)
#
## Bugs in development
- At first the workspace couldn't create the profile app error-message "can't open file 'manage.py': [Errno 2] No such file or directory".
   - File existed
   - File was located inside a p5_api folder, when the project folder ws created it created double folders, put the manage.py-file inside the first folder next to
     the second p5_api-folder that contained all the python files for the project.
   - Solution: Move all files outside both folders, delete the inner p5_api-folder, move all python-files but the manage.py file inside the one remaining p5_api folder. Create app.
   - App successfully created.
- During initial deployment to Heroku.
    - Error message: application error
    - Solution: With the help of Tutor support we found spelling errors in multiple places of allowed hosts. When these where solved deployment was successfull. 
- In initial deployment to Heroku, app did not launch. 
  - Looked through code to spot typos and typos in heroku settings. Found a couple, with the help of Gemma at tutor support, also hard set the allowed hosts to the heroku url.
- After the workspace timed out and was deleted, couldn't get the preview to run, after creating a new env-file from Heroku Config Vars.
   - solution reinstall dependencies with 'pip3 install -r requirements.txt'.
- In production of chat application, several error messages occured. Most had to do with naming and missing routes between files, but one was a OperationalError, tht did not want to resolve itself with convential methods.
   - Solved using a database reset script given by Tutor support.
   The script:
      - Renamed the old sql-database to sqlite3.old.
      - Remove all migration files
      - Make new migrations
- No connection between connection in model Contacts and model Messages.
   - Solved by moving up all model settings to Contacts to ensure fluidity between the two sections. Security and privacy for Chat-User will be ensured using authentication methods in React.
      - Possible improvement might be using permission_required and/or a PermissionRequiredMixin from [Django authentication decorators](https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-permission-required-decorator).
- While testing messages no unique id created for each message, since Chatdetail with Contactlist works the same as Commentdetail with Commentlist. User only able to edit first message.
   - Solution: split the contacts and messages into two seperate apps.
- In the new app, first named messages, it clashed with a django code named messages, creating duplicates in when running server.
   - Solution: change name to imessage, plus related fields.
- When creating path between contacts/models.py and imessages/models.py, several bugs in connecting the two.
   - Solution: with owner let that be a User from the Django library, with contact let that be imported from contacts/models.py, also save the new messages in imessages/views.py function def perform_create.
- Accessing pagination in preview renders a faulty url (http://localhost:8000/likes/?page=3), but works if you hardwrite correct url in url-window (https://8000-mikakallber-projectport-0e5hagl364b.ws-eu71.gitpod.io/likes/?page=3). Tutor support concluded that it might not be a problem for front end use, since that access correct url. Unclear if it's an actual bug, but something to keep in mind. 
   - If problem arises in front end reffer to chat with tutor support and this link: https://stackoverflow.com/questions/33202137/localhost-rejecting-connection-from-application
- While developing the Front-End part of this project I couldn't get post_cpunt, following_count and follow_count to work in the profile.
   - These fields where not added to profiles/serializers.py. 
   - Added items and bug resolved.
#
## Bugs left unsolved
- In settings.py the following bugs is left unsolved:
   - 're' imported but unused
      - It is not being unused [Python docs on re](https://docs.python.org/3/library/re.html).
   -'env' imported but unused
      - The env is in an if statement and is therefore under conditional use. In localhost as in preview the env-file is implemented,
        where as in Heroku cofig vars are used.
   - 4 line to long on line 102, 105, 108 and 111. 
      - These can't be modified, since doing so will create a more serious error that affects functionality.
- Pylints:

#
* [Back to top](#)
#