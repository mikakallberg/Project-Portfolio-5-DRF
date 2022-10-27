# Social Media API
* [Deployed Front-End page](https://cozycorner-pp5.herokuapp.com/)
* [Deployed Back-End page](https://portfolio-project-5-drf-api.herokuapp.com/)
#
## Navigation
#
* [Bugs](/bugs.md)
   - [Bugs in development](/bugs.md#bugs-in-development)
   - [Bugs left unsolved](/bugs.md#bugs-left-unsolved)
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
    - [First setup](#first-setup)
    - [Testing in development](#testing-in-development)
    - [Profile](#profile)
    - [Post](#post)
    - [Comments](#comments)
    - [Likes](#likes)
    - [Followers](#followers)
    - [Messages](#messages)
    - [Contacts](#contacts)
* [User Experience](/README.md#user-experience-ux)
    - [Demographics](/README.md#demographics)
    - [User Goal](/README.md#user-goals)
#
## First setup
- Testing done to ensure successful initial launch in preview and functionality of profiles app.
- Test also successfull in Heroku.
#
Launch Successful in preview                         |
:--------------------------------------------------: | 
 ![Launch](/assets/images_readme/launch_success.jpeg)|
#
Successfull launch in Heroku                        |
:--------------------------------------------------:|
  ![Herokku launch](/assets/images_readme/heroku_success_test.jpeg)

#
## Testing in development
- After creation of a superuser.
   -Test to see that /admin worked and that admin view is running correctly
   - created 4 other profiles
      - Test if default image works
      - Test if password requirements work
- Images below are only a sample of all the testing done
- Testing responsiveness with [AmIResponsive](https://ui.dev/amiresponsive?url=https://cozycorner-pp5.herokuapp.com/)
- When trying to test for PEP8 conformity, the webpage http://pep8online.com/ is no longer active.
    - However the code conforms to the way taught in lesson material from Code Institute
#
Admin view testing                                            |
:------------------------------------------------------------:| 
![Password requirement](assets/images_readme/password_req.png)|
#
Profiles created in admin view, has default image              |
:-------------------------------------------------------------:|
![Profiles](assets/images_readme/profiles_created_in_admin.png)|
#
## Profile
- Testing done on profile:
   - Possible for superuser to edit user profile in UI
      - Other non-superusers cannot change info on other users
      - Other non-superusers cannot access admin-panel
      - Testing done on profile 1, 3 and 5 after adding authentication. Testing also in logged out state. Only owner can access edit tool for profile
   -After refactoring:
      - test delete profile, successfull
      - No access to delete other users profiles
   - Test filtering profiles:
       - after which profile is following who and order in descending and ascending order for follow count, post count, owner following created at
       - profiles following other profiles or not and then ordering then differently ascending and descending order.
   - Access non existent profile
      - 404 does not exist
#
Profile list logged in view                                  | Profile list not logged in view 
:----------------------------------------------------------: | :------------------------------------------------------------:
 ![Profile list](/assets/images_readme/profiles_loggedin.png)| ![Profiles list](/assets/images_readme/profiles_loggedout.png)
#
Profile detail owner                                        | Profile detail not owner
:----------------------------------------------------------:| :-------------------------------------------------------------:
 ![Profile detail](/assets/images_readme/profile_owner.png) | ![Profiles detail](/assets/images_readme/profile_notowner.png)
#
Profile created in admin                                                | Profile detail deleted profile
:----------------------------------------------------------------------:| :---------------------------------------------------------------:
 ![Profile created](/assets/images_readme/profiles_created_in_admin.png)| ![Profile deleted](/assets/images_readme/test_delete_profile.png)
#
Profile doesn't exists                                     | Wrong password
:---------------------------------------------------------:| :---------------------------------------------------------:
 ![No profile](/assets/images_readme/profile_noprofile.png)| ![Wrong password](/assets/images_readme/wrong_password.png)
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
      - test entire CRUD functionality and view from non-owner view
   - After adding like_id to posts, testing to see if create and delete like functions successfully.
   - Test filtering functions.
       - Order posts on number of likes, number of comments and when posts where liked. 
       - Filtering on profiles a user is following, likes and posts
   - Access non existent post
      - 404 does not exist
#
Postlist                                              | Postdetail notowner
:---------------------------------------------------: | :-------------------------------------------------------------:
 ![Post list](/assets/images_readme/post_list_two.png)| ![Post detail](/assets/images_readme/post_detail_notowner.png)
#
Post owner delete access                                         | Postdetail deleted
:--------------------------------------------------------------: | :-----------------------------------------------------:
 ![Postowner](/assets/images_readme/postdetail_delete_access.png)| ![Post deleted](/assets/images_readme/deleted_post.png)
#
Post owner edit                                                  | Postdetail no post
:--------------------------------------------------------------: | :--------------------------------------------------------------:
 ![Postedit](/assets/images_readme/test_edit_post.png)           | ![Post no post](/assets/images_readme/test_404_post_detail.png)
#
 Post error image size byte                                        | Post error image size pixels 
:----------------------------------------------------------------: | :---------------------------------------------------------------:
 ![Error image](/assets/images_readme/error_postimagesizebyte.png) | ![Error image](/assets/images_readme/error_postimagesizepx.png)
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
   - Access non existent comment
      - 404 does not exist
#
Commentlist                                              | Commentdetail owner
:------------------------------------------------------: | :-------------------------------------------------------------:
 ![Commentlist](/assets/images_readme/comment_list.png)  | ![Commentdetail](/assets/images_readme/commentdetail_owner.png)
#
Comment not owner                                                   | Comment detail edit/delete
:-----------------------------------------------------------------: | :--------------------------------------------------------------------------:
 ![Comment not owner](/assets/images_readme/comment_not_owner.png)  | ![Commentdetail edit/delete](/assets/images_readme/delete_comment_owner.png)
#
## Likes
- Testing done on like:
   - Unauthenticated users
      - No access to liking posts
   - Authenticated users can like posts
      - Successfull
      -Error if duplicate like attempted
   - Authenticated and authorized user can delete like
      - Successfull
   - Access non existent like
      - 404 does not exist
#
Likelist                                           | Like and comment count
:------------------------------------------------: | :-------------------------------------------------------------------------:
 ![Likelist](/assets/images_readme/like_list.png)  | ![Like and comment count](/assets/images_readme/like_and_comment_count.png)
#
Likedetail owner                                                  | Likedetail not owner
:---------------------------------------------------------------: | :-------------------------------------------------------------:
 ![Likedetail owner](/assets/images_readme/likedetail_owner.png)  | ![Likedetail not owner](/assets/images_readme/likedetail_not_owner.png)
#
Deleted like access                                                    | Deleted like
:--------------------------------------------------------------------: | :------------------------------------------------------:
 ![Deleted like access](/assets/images_readme/delete_like_access.png)  | ![Deleted like](/assets/images_readme/deleted_like.png)
#
Like duplication                                                      |
:--------------------------------------------------------------------:|                                                
![Like duplication](/assets/images_readme/like_duplication.png)       |
#
## Followers
- Testing done on followers:
   - Test following authenticated users as a authenticated user
   - No access to follow authenticated user while not logged in
   - Successful unfollowing a authentictated user as a logged in user
   - A user can't remove an authenticated User from their followers list
      - Possible improvement
   - Access non existent follow
      - 404 does not exist
#
Follow list                                              | Follower create
:------------------------------------------------------: | :-------------------------------------------------------------:
 ![Follow list](/assets/images_readme/followerlist.png)  | ![Follower create](/assets/images_readme/follow_create.png)
#
Follower delete                                                | Followerdetail owner
:------------------------------------------------------------: | :-------------------------------------------------------------------:
 ![Follower delete](/assets/images_readme/follow_deleted.png)  | ![Followerdetail owner](/assets/images_readme/followdetail_owner.png)
#
Followerdetail not owner                                                       |
:-----------------------------------------------------------------------------:|
![Followerdetail not owner ](/assets/images_readme/followerdetail_notowner.png)|
#
## Messages
- Testing done on imessages:
   - User need to be logged in to access view
      - Successfull 
      - Shows 404 page if user is not logged in
   - User can initiate contact with another User
      - Successfull
   - That contact can then be transfered to imessages and connect creating a message to the User(owner) and User(contact), with unique Ids on owner, contact and message
      - Successfull, but severed connection because the path Id becomes cleaner if both contact and owner originates from imessages, instead of adding another layer of Id with contacts. 
      - Id initiated in contacts can be used to create multiple person chat rooms instead.
   - User that is owner can access message and has access to edit or delete message
      - Successfull
   - User that is not owner cannot access edit or delete function
      - Successfull
   - Message is successfully saved and error message for image file works, both for byte-size and px-size.
      - Successfull
   - Access non existent message
      - 404 does not exist

#
Messagedetail owner                                                | Messagedetail not owner
:----------------------------------------------------------------: | :---------------------------------------------------------------------------:
 ![Messagedetail owner](/assets/images_readme/message_detail.png)  | ![Messagedetail not owner](/assets/images_readme/messagedetail_notowner.png)
#
Messagedeleted                                                       | Messagelist
:------------------------------------------------------------------: | :-----------------------------------------------------------------:
 ![Messagedeleted](/assets/images_readme/messagedetail_deleted.png)  | ![Messagelist](/assets/images_readme/message_muitple_contacts.png)
#
Message error image size byte                                   | Message error image size pixels 
:-------------------------------------------------------------: | :-------------------------------------------------------------------:
 ![Error image](/assets/images_readme/error_imagesize_byte.png) | ![Error image](/assets/images_readme/error_imagesizepx.png)
#
No default image in message                                                       |
:--------------------------------------------------------------------------------:| 
 ![No default image in message](/assets/images_readme/nodefault_image_message.png)|
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
   - Access non existent contact
      - 404 does not exist
#
Contactdetail owner                                                     | Contactdetail not owner
:---------------------------------------------------------------------: | :---------------------------------------------------------------------------:
 ![Contactdetail owner](/assets/images_readme/contactdetail_owner.png)  | ![Contactdetail not owner](/assets/images_readme/contactdetail_notowner.png)
#
Contactdeleted                                                                   | Contact create contact
:------------------------------------------------------------------------------: | :-------------------------------------------------------------------:
 ![Contactdeleted](/assets/images_readme/contactdetail_delete_confirmation.png)  | ![Contact create contact](/assets/images_readme/contact_adname.png)
#
View not logged in for both Contact and message                                  | Contactlist
:------------------------------------------------------------------------------: | :----------------------------------------------------:
 ![Notlogged in](/assets/images_readme/view_not_loggedin_contacts_imessage.png)  | ![Contactlist](/assets/images_readme/contactlist.png)
#
* [Back to top](#)
#