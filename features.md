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
   - [Existing Features](#existing-features)
        - [Profile](#profile)
        - [Post](#post)
        - [Comments](#comments)
        - [Likes](#likes)
        - [Followers](#followers)
        - [Messages](#messages)
        - [Contacts](#contacts)
   - [New Features](#new-features)
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
## Existing Features
### Profile
- Anonymous User can register and create a profile
- Users can log in to their profile
- Users can see registered profiles
- Users can see a list of other Users
- Users can see the a detail view of other users
#
### Post
- Anonymous User and registered Users can see public posts
- Users can create posts with or without images
- Users can edit posts that they own
- Users can delete posts that they own
#
### Comments
- Anonymous User and Users can see public comments
- Users can create a comment on a post
- Users can edit a comment they have created
- Users can delete a comment they have created
#
### Likes
- Anonymous User and Users can see likes on posts
- Users can like a post
- Users can unlike a post
#
### Followers
- Anonymous User and Users can see followers
- Users can follow a User
- Users can unfollow a User
#
### Messages
- If user is logged in they can access messages
- Users can connect with other Users
- Users can create a message to another user with or without a image
- Users can edit a message they have sent to another user
- users can delete a message they have sent to another user
#
### Contacts
- If user is logged in they can access contacts
- Users can connect with other Users
- Users can name this connection
#
## New Features
#
- Give User control of their followers list, by adding delete and/or block function.
- In the chat feature (apps contacts and imessage) use permission_required and/or a PermissionRequiredMixin from [Django authentication decorators](https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-permission-required-decorator). To increase User control over who they connect with.
- Adding Search filter to imessages and or contacts, to give Usser the possibillity to search among their chats and contacts.

#
* [Back to top](#)
#