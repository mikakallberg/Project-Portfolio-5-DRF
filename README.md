# Social Media API

![Am I Responsive](/assets/images_readme/amiresponsive.png)
#
* [Deployed Front-End page](https://cozycorner-pp5.herokuapp.com/)
* [Deployed Back-End page](https://portfolio-project-5-drf-api.herokuapp.com/)
#
## Navigation
Please note that this documentation has multiple pages
* [Bugs](/bugs.md)
    - [Bugs in development](/bugs.md#bugs-in-development)
    - [Bugs left unsolved](/bugs.md#bugs-left-unsolved)
* [Credits](#credits)
    - [Mentoring](#thank-you)
    - [Content credits](#content-credits)
    - [Media](#media) 
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
* [Learning Outcomes](#learning-outcomes)
* [Planning](#planning)
   - [Initial planning](#initial-plan)
   - [Plan](#plan)
   - [Lucid Chart](#lucidchart)
* [SetUp](/setup.md)
   - [Set up repository](/setup.md#set-up-repository)
   - [Set up project in GitPod](/setup.md#set-up-project-in-gitpod)
   - [Set up unique model in Gitpod](/setup.md#set-up-unique-model-in-gitpod)
* [Technologies and Libraries](#technologies-and-libraries)
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
* [User Experience](#user-experience-ux)
    - [Demographics](#demographics)
    - [User Goal](#user-goals)

 
#
## Project Goals
- Design an interactive Front-End web application using HTML, CSS and advanced JavaScript, based on component composition and separation of concerns.
   - For more information see [Front-End Repository](https://github.com/mikakallberg/cozycorner)
- Explain the key role that specialist Front-End developers perform in modern software development/delivery terms.
- Create an Application Programming Interface (current repository) for comsumption by 3rd party applications.
   - Create Unique models.
      - Number of models created four, two in contacts and two in imessages.
- Create an Interactive Front-End application that consumes API data.
#
## Technologies and Libraries
### Languages used
- [Django Rest Framework](https://www.django-rest-framework.org/) 

- [HTML](https://www.w3schools.com/html/html_intro.asp)

- [CSS](https://www.w3schools.com/css/css_intro.asp)

- [React JS](https://reactjs.org/)

### Databases and server gateways
- [Postgresql](https://www.postgresql.org/)
  - As database in Heroku
- [SQLite](https://www.sqlite.org/index.html)
  - As database for Gitpod, the initial thought was to use this for unittest.
  The setting is left as part of future features, to have automatic testing instead of manual testing
- [Daphne ASGI](https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/daphne/)

### Frameworks, tools and libraries
#### Back-End
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Channels-redis](https://channels.readthedocs.io/en/latest/index.html) 
   - Websocket tool
- [Pillow](https://pillow.readthedocs.io/en/stable/reference/Image.html)
   - To assist upload images to cloudinary
- [Psycopg2](https://pypi.org/project/psycopg2/)
   - PostgreSQL database adapter for python
- [JSON Web Tokens](https://jwt.io/)
   - Http-safety, web-tokens for kepping user logged in, authentication etc.
#### Front-End
- [React JS](https://reactjs.org/)
- [JSON Web Tokens](https://jwt.io/)
    - Web-tokens for kepping user logged in, authentication etc.
- [React Bootstrap](https://react-bootstrap-v4.netlify.app/)
   - Specilaize Bootstrap framework with React components
- [React Router](https://v5.reactrouter.com/web/guides/quick-start)
   - Assist in switches, routes and links for React apps.


### Cloud storage and deployment services
- [Cloudinary](https://cloudinary.com/)
- [Heroku](https://www.heroku.com/)
- [Gunicorn](https://gunicorn.org/)

#
## Planning
### Initial plan
#
Initially this project was planned as a planner tool, but after consulting  my mentor, it was switched to follow the walkthrough from the lessons on Rest-framework and React. The wireframe for that initial plan can be found if you follow this link: https://mikakallberg.github.io/wireframe-planner/
#
### Plan
#
- The current direction for this project is to follow the walkthrough given by Code Institute and add two unique models. These are Message in app imessages and Contacts in contacts. Which where added to give the User an opurtunity to message other Users directly and have private conversations.
#
### LucidChart
#
![LucidChart](/assets/images_readme/lucidchart.png)
#
## Demographics
- The intended user for this API is someone who wants to build a Front-End application consistent with the below stated [User Goals](#user-goals).
#
## User Goals
#
- As a Site User I can register an account 
- As a Site user I can delete my account
- As a Site User I can Create Posts
- As a Site User I can Edit and Delete that Post at will
- As a Site User I can Follow and Unfollow other Users
- As a Site User I can Comment on other Users Posts
- As a Site User I can Edit and Delete the Comment I own
- As a Site User I can Like and Unlike Posts from other Users Posts
- As a Site User I can Create Contacts with other Users, with or without a name.
- As a Site User I can Edit and  Delete Contacts with other Users, with or without a name.
- As a Site User I can Create Messages with other Users
- As a Site User I can Edit and Delete Messages I sent to other Users

## Credits
## Thank you
- [Spencer Barriball](https://github.com/5pence) for always being there and being a fantastic mentor.
- Tutors at Code Institute
- Code Institute Slack-channel community for being the good and funny bunch of people I need!


### Content credits
- For unique models a walkthru video from the account [Code With Stein](https://www.youtube.com/watch?v=SF1k_Twr9cg) was used. However current project is not exactly the same, the biggest difference is the walkthru is a one to many relationship, while the chat function in this project is mainly a one to one relationship. Howevere there is a possibility to expand the app named contacts to include a one to many chat.

### Media
- For how to make the README nav-bar https://github.com/artkonekt/menu/blob/master/README.md was used.
- As template for README https://github.com/mikakallberg/Portfolio-Project-4 was used.

#
* [Back to top](#)
#