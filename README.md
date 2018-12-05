# Issue Tracker  
Tracks bugs and feature requests for an App.
User participation in requests and voting is recorded.
Payment method included for requested features.

## UX
Home page gives a brief explanation of the App and advises users to use the nav links.
Nav links for signed in users allow direct access to all of the App features



## Features

### Existing Features
- User can view, create, comment, edit, vote and delete issues
- User can create an issue as either a bug or a requested feature
- Admin/user shows progress of issue by dates: created, accepted, started, completed
- User can pay for a feature using stripe credit card processing
- User profile page shows issues voted/created and features paid


### Features Left to Implement
- Improve comment section - seperate line for each comment with creator name
- Make a user status level based on profile page data. Award points for each action.
- Graphical display of issues status

## Technologies Used

- [Django] (https://www.djangoproject.com/)
    - framework used for this project
- [Postgres] (https://www.postgresql.org/)
    - object-relational database management system 
- [Python 3] ( https://www.python.org/ )
    - This project is python driven.
- [Bootstrap] ( http://getbootstrap.com// )
   - The styling library
==================
- [JQuery](https://jquery.com)
    - Generates 
- [d3] (https://d3js.org/) . 
    - Used to draw the graphs 
- [queue] (https://cdnjs.com/libraries/queue-async). 
    - Loads data from stored file for d3 use.
======================
 


## Testing

### Tests

1. All nav links tested and correct
2. login/logout tested
   -Appropriate nav links appear for logged in/out user
3. 
    


### Devices
    - Tested on google inspect for different screen sizes. No issues found.
    - Tested on browsers Chrome, Edge, Opera.

### Issues:
1. Bugs:
    1. when issue deleted, corresponding user profile data not deleted. 
    

## Deployment:

1. App deployed on Heroku: https://project5-tracker.herokuapp.com/
2. Files created for this deployment: Procfile, requirements.txt.
3. Packages installed for deployment: dj-database-url, psycopg2, whitenoise

## Credits
1. Stackoverflow -for so many things.
2. https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

