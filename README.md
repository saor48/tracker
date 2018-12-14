# Issue Tracker  
Tracks bugs and feature requests for an App.
User participation in requests and voting is recorded.
Payment method included for requested features.

## UX
Home page gives a brief explanation of the App and advises users to use the nav links.
Nav links for signed in users allow direct access to all of the App features
Prominent buttons allow users to take actions such as vote, edit, delete.


## Features

### Existing Features
- User can view, comment and vote on any issue
- Only issue creator can edit and delete issue
- User can create an issue as either a bug or a requested feature
- Admin shows progress of issue by dates: created, accepted, started, completed
- User can pay for a feature using stripe credit card processing
- User profile page shows issues voted/created and features paid


### Features Left to Implement
- Make a user status level based on profile page data. Award points for each action.

## Technologies Used

- [Django] (https://www.djangoproject.com/)
    - framework used for this project
- [Postgres] (https://www.postgresql.org/)
    - object-relational database management system 
- [Python 3] ( https://www.python.org/ )
    - This project is python driven.
- [Bootstrap] ( http://getbootstrap.com// )
   - The styling library
- [JQuery] (https://jquery.com)
    - Used on graphs page to grab data for d3
    - Used on edit page with jquery themes for datepicker
- [d3] (https://d3js.org/) . 
    - Used to draw the graphs 


## Testing

### Tests

1. All nav links tested and correct page reached
2. login/logout tested
   -Appropriate nav links appear for logged in/out user
3. Issues page
    1. Vote button 
        1. records vote by correct id on profile page
        2. shows error message if issue already voted on
    2. Edit button
        1. Shows error message if user is not issue owner
        2. if user is owner brings up edit page with correct issue
    3. View Comments button
        1. Shows comments for correct issue
4. Edit page
    
    


### Devices
    - Tested on google inspect for different screen sizes. No issues found.
    - Tested on browsers Chrome, Edge, Opera.

### Issues:
1. Improvements needed for:
    1. when issue deleted, corresponding user profile data not deleted. 
    

## Deployment:

1. App deployed on Heroku: https://project5-tracker.herokuapp.com/
2. Files created for this deployment: Procfile, requirements.txt.
3. Env var values removed from settings and put in Heroku Settings - Config Vars
4. Packages installed for deployment: dj-database-url, psycopg2, whitenoise
5. https://github.com/saor48/tracker.git

## Credits
1. Stackoverflow -for so many things.
2. https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

