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
- Change latest activity date on Profile to show previous last activity date
- Show name of logged in user in nav bar


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
        1. Brings up commentary page (/comments/comments.html) for correct issue
4. Edit page
    1. Delete button deletes correct issue
    2. Submit button 
        1. edits correct issue
        2. only edits date fields (stated at top of form), ignores other fields
        3. correct dates recorded
5. Commentary page (show all comments for an issue )
    1. Heading shows correct issue
    2. Comments are oldest first as expected.
    3. Comment button brings up make a comment form (/issues/comment.html) for correct issue
6. Comment page (add a comment)
    1. shows correct issue name and description
    2. Submit button records comment, user and date correctly and ignores other form fields
    3. submit blank comment has no effect
7. Profile page
    1. Drop down menu in Payment box shows expected behaviour : 
        - shows only features in Voted Features but not in Paid features
    2. Pay Button brings up Payment form with correct issue and price.
    3. Correct issue id appears in Paid Features after successful payment
    4. Blank input for Pay button shows required error message.
8. Payment page
    1. Works as expected
    2. Returns correct id to profile page if payment successful.
    3. If payment unsuccessful this id does not appear in profile Paid Features
9. Create Issue page
    1. Submit Issue Button records issue correctly.
10. Graphs page
    1. graphs have correct numeric and bar chart values.

### Devices
    - Tested on google inspect for different screen sizes. No issues found.
    - Tested on browsers Chrome, Edge, Opera.

### Issues:
1. Improvements needed for:
    1. when issue deleted, corresponding user profile data not deleted. 
2. Data stored in strings should be instead in seperate fields SQL style.
    - I was still thinking Mongo style when starting this project.    

## Deployment:

1. App deployed on Heroku: https://project5-tracker.herokuapp.com/
    1. Add postgres database: In heroku-Resources-Add Ons; 
        - type 'postgres', click on item that appears and follow menu.
    2. Add config vars: in Heroku-Settings-Reveal Config Vars
        - copy STRIPE_SECRET, STRIPE_PUBLISHABLE and SECRET_KEY from c9 env.py 
        - also add DISABLE_COLLECTSTATIC with value 1
        - copy DATABASE_URL from here back to c9 env.py
    3. Add 'project5-tracker.herokuapp.com' to c9 Settings-Allowed Hosts
    4. Create new superuser for postgres database.
2. Packages installed for deployment: dj-database-url, gunicorn, psycopg2, whitenoise
3. Files created for this deployment: Procfile, requirements.txt.
    -echo web: gunicorn tracker.wsgi:application > Procfile
    -pip3 freeze --local > requirements.txt
4. Comment out 'import env' in c9 Settings before doing git add to keep secret those values
5. GitHub Repository: https://github.com/saor48/tracker.git

## Credits
1. Stackoverflow -for so many things.
2. https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

