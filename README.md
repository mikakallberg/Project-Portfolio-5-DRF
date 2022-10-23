# Social Media API

![Am I Responsive]()
## Navigation Through Content
#
* [Deployed page]()
* [Project Purpose](#project-purpose)
    - [Learning Outcomes](#learning-outcomes)
* [Initial Planning](/deployment.md)
* [Initial SetUp](/setup.md)
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
#
## Learning Outcomes
- Design an interactive Front-End web application using HTML, CSS and advanced JavaScript, based on component composition and separation of concerns.
   - For more information see [Front-End Repository]()<--- Put in link when done!
- Explain the key role that specialist Front-End developers perform in modern software development/delivery terms.
- Create an Application Programming Interface (current repository) for comsumption by 3rd party applications.
   - Create Unique models.
      - Number of models created four, two in contacts and two in imessages.
      - models in contacts can be developed into one more for a group chat.
- Create an Interactive Front-End application that consumes API data.
#
## Technologies and Libraries used

### Languages used
- [Django](https://www.djangoproject.com/) 

- [HTML](https://www.w3schools.com/html/html_intro.asp)

- [CSS](https://www.w3schools.com/css/css_intro.asp)

- [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)

### Databases
- [Postgresql](https://www.postgresql.org/)
  - As database in Heroku
- [SQLite](https://www.sqlite.org/index.html)
  - As database for Gitpod, the initial thought was to use this for unittest.
  The setting is left as part of future features, to have automatic testing instead of manual testing

### Frameworks and tools
- [Bootstrap](https://getbootstrap.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Summernote](https://summernote.org/)
- [Fontawesome](https://fontawesome.com/)
- [Django-Crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django-Copyright](https://pypi.org/project/django-copyright/)
- [Google fonts](https://fonts.google.com/specimen/Playfair+Display?category=Serif,Sans+Serif#standard-styles)
- [Channels with Dahpne ASGI](https://channels.readthedocs.io/en/latest/index.html)

### Cloud storage and deployment services
- [Cloudinary](https://cloudinary.com/)
- [Heroku](https://www.heroku.com/)
- [Gunicorn](https://gunicorn.org/)

#
## Planning
#
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

## User Experience (UX)
#
## Demographics
- The intended user for this API is someone who wants to build a front end view consistent with the below stated [User Goals](#user-goals).


## User Goals
#
- As a Site User I can register an account 
- As a Site user I can delete my account
- As a Site User I can Create Posts with or without images
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
#
## Thank you
- [Spencer Barriball](https://github.com/5pence) for always being there and being a fantastic mentor.
- Tutors at Code Institute
- Code Institute Slack-channel community for being the good and funny bunch of people I need!


### Content credits
- For unique models a walkthru video from the account [Code With Stein](https://www.youtube.com/watch?v=SF1k_Twr9cg) was used. However current project is not an exactly the same, the biggest difference is walkthru is a one to many, while this project is one to one.

### Media
- For how to make the README nav-bar https://github.com/artkonekt/menu/blob/master/README.md was used.
- As template for README https://github.com/mikakallberg/Portfolio-Project-4 was used.

#
* [Back to top](#)
#