Begin Development: 1. git clone the repo 2. create and activate virtual environment (python3 -m venv venv ::: source venv/bin/activate) 3. download reqs (pip install -r requirements.txt) 4. pip freeze ideally DEV GUIDE: Our project has 3 apps: 1. core Core is the login and home screen of the app. The html for these sites can be found in core/templates 

To stay up to date on the project:  
Check what branch you are currently in (git branch). Make sure you're in master; if not, switch over (git checkout master). Then update master for the latest changes (git pull origin master).

To develop on this project:  
Create your own branch (git checkout -b my-branch-name). Make sure you're on your branch (git branch). Push your branch to GitHub (git push -u origin my-branch-name).

To merge your work into master:  
Push your latest changes (git push). Open a Pull Request on GitHub and wait for the team to review it.

2. note_page Note view page is the page where you will view all of the user notes (as seen in the n notes figure in the disc) and click in to edit them Edit note page is where you edit notes, also will be ideally as seen in the images 3. calendar_page Calendar page is where you will view the calendar. This one might be goofy as we also want the calendar to render in the home page which is why it's it's own app. Will be weird to figure that out but that's something we will figure out at the end.


Current Webpage layout: 

    Welcome Page ( login/sign-up)
    Home Page ( User dashboard, view )
    Notes Page ( Users Notes, Create a note, Edit note, Delete note ) * in process * 
    Calendar page ( Calendar Months, Add Event Feature, 
    Account page ( Users information, change password, account deletion) 


TO-DO / Additional Features ideas: 

Home Page: add calendar to dashboard (can be a smaller calendar or just drop-down feature of calendar events), display notebooks or classes on dashboard, upon clicking will take user to notes page, add user customization (background design or color, grab to customize layout, adjust size of cards ). Other ideas: Stop watch, calculator, to-do card for upcoming assignemnts or tasks ( maybe its own page ). 

Notes Page: create a note, edit a note, and delete a note. Notes will be placed into notebooks or classes, so it will be like title and then body. but the title will be the notebook and thats what will show in the dashboard. other features: file uploader, upload a screenshot or photo. 

Calendar: add event, events should have a date, time, and title, maybe description. Edit or delete an event option. Customize the calendar ( color code different event types, design the calendar). drag and drop feature for events. other feature: notification system alerts on events.

Account page: Change email, change password options and account deletion option along with are you sure message.



Make sure to refer to the Study Helper Layout Guide for any page development, although it may need an update it still has some guidance in the meantime: 
https://uofnebraska-my.sharepoint.com/:w:/r/personal/96585664_nebraska_edu/Documents/Study%20Helper%20Layout.docx?d=w5443d516d9c446508ab7ef59078a4177&csf=1&web=1&e=oRQdyC

There is also the notion Study-guide progress tracker:
https://www.notion.so/Project-Tracker-c07ffb5a8f058277935501db25edb6dc?source=copy_link

Data Model Diagram:
https://lucid.app/lucidchart/88f1d29f-e18c-48fe-bc2c-bcd70ed60b63/edit?viewport_loc=497%2C-9%2C1303%2C1004%2C0_0&invitatio
