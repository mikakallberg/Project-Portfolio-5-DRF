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
   - [Set up repository](/setup.md#set-up-repository)
   - [Set up project in GitPod](/setup.md#set-up-project-in-gitpod)
   - [Set up unique model in Gitpod](/setup.md#set-up-unique-model-in-gitpod)
* [User Experience](/README.md#user-experience-ux)
    - [Demographics](/README.md#demographics)
    - [User Goal](/README.md#user-goals)
* [Features](/features.md)
   - [Existing features](/features.md#existing-features)
   - [Possible improvements](/features.md#features-left-to-implement)
* [Testing](/testing.md)
    - [First setup](#first-setup)
    - [Testing in development](#testing-in-development)
    - [Profile](#profile)
    - [Post](#post)
    - [Comments](#comments)
    - [Likes](#likes)
    - [Followers](#followers)
    - [Messages](#messages)
    - [Contacts](#contacts)
* [Bugs](/bugs.md)
* [Deployment](/deployment.md)
* [Credits](/README.md#credits)
    - [Mentoring](/README.md#thank-you)
    - [Content credits](/README.md#content-credits)
    - [Media](/README.md#media)  
#
## First setup
#
- Testing done to ensure successful initial launch in preview and functionality of profiles app.
- Test also successfull in Heroku.
#
Launch Successful in preview                         | Profiles succesfull
:--------------------------------------------------: | :--------------------------------------------------:
 ![Launch](/assets/images_readme/launch_success.jpeg)| ![Profiles test](/assets/images_readme/first_profile_test.jpeg)
#
Successfull launch in Heroku                        |
:--------------------------------------------------:|
  ![Herokku launch](/assets/images_readme/heroku_success_test.jpeg)

#
## Testing in development
#
- After creation of a superuser.
   -Test to see that /admin worked and that admin view is running correctly
   - created 4 other profiles
      - Test if default image works
      - Test if password requirements work.
#
Admin view testing  
   ![Password requirement](assets/images_readme/password_req.png)
#
Profiles created in admin view, has default image
   ![Profiles](assets/images_readme/profiles_created_in_admin.png)
#
## Profile
- Testing done on profile:
   - Possible for superuser to edit user profile in UI
      - Other non-superusers cannot change info on other users.
      - Testing done on profile 1, 3 and 5 after adding authentication. Testing also in logged out state. Only owner can access edit tool for profile
   -After refactoring:
      - test delete profile, successfull
      - No access to delete other users profiles
   - Test filtering profiles:
       - after which profile is following who and order in descending and ascending order for follow count, post count, owner following created at
       - profiles following other profiles or not and then ordering then differently ascending and descending order.
#
- Images
#
## Post
- Testing done on post:
   - Unathorized user creating posts
      - No access to tools
   - Post is successfully saved and error message for image file works, both for byte-size and px-size.
      - Successfull
   - Not filling out title-field
      -Error message
   - View for other authorized users, no edit functionality on posts
      - Successfull
   - After refactoring:
      - test entire crud functionality and view from non-owner view
   - After adding like_id to posts, testing to see if create and delete like functions successfully.
   - Test filtering functions.
       - Order posts on number of likes, number of comments and when posts where liked. 
       - Filtering on profiles a user is following, likes and posts
#
- Images
#
## Comments
- Testing done on comments:
   - Creating, editing and deleting post as authorized user.
      - Successful
   -Accessing comment as other authenticated user 
      - Read only.
   - Accessing comment as unathenticated user 
      - Read only.
   - Test filtering comments of different user's posts
      - Successfull
#
- Images
#
## Likes
- Testing done on like:
   - Unauthenticated users
      - No access to liking posts
   - Authenticated users can like posts
      - Successfull
      -If tried twice error-page.
   - Authenticated and authorized user can delete like
      - Successfull
#
- Images
#
## Followers
- Testing done on followers:
   - Test following authenticated users as a authenticated user
   - No access to follow authenticated user while not logged in
   - Successful unfollowing a authentictated user as a logged in user
   - A user can't remove an authenticated User from their followers list
      - Possible improvement
#
- Images
#
## Messages
- Testing done on imessages:
   - User need to be logged in to access view
      - Successfull 
      - Shows 404 page if user is not logged in
   - User can initiate contact with another User
      - Successfull
   - That contact can then be transfered to imessages and connect creating a message to the User(owner) and User(contact), with unique Ids on owner, contact and message
      - Successfull, but severed connection because the path Id path becomes cleaner if both contact and owner originates from imessages, instead of adding another layer of Id with contacts. 
      - Id initiated in contacts can be used to create multiple person chat rooms instead.
   - User that is owner can access message and has the opurtunity to edit or delete message
      - Successfull
   - User that is not owner cannot access edit or delete function
      - Successfull
   - Message is successfully saved and error message for image file works, both for byte-size and px-size.
      - Successfull

#
- Images
#
## Contacts
- Testing done on contacts:
   - User need to be logged in to access view
      - Successfull
      - Shows 404 page if user is not logged in
   - User can initiate contact with another User
      - Successfull
   - User can remove their contact with another User
      - Successfull
#
- Images
#
* [Back to top](#)
#