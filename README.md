TO DEVELOP ON THIS:
    1. git clone the repo
    2. activate the virtual env (source web_env/bin/activate)
    3. download reqs (pip install -r requirements.txt)
    4. pip freeze ideally
DEV GUIDE:
    Our project has 3 apps:
        1. core
            Core is the login and home screen of the app. The html for these sites can be found in core/templates
        2. note_page
            Note view page is the page where you will view all of the user notes (as seen in the n notes figure in the disc) and click in to edit them
            Edit note page is where you edit notes, also will be ideally as seen in the images
        3. calendar_page
            Calendar page is where you will view the calendar. This one might be goofy as we also want the calendar to render in the home page which is why it's it's own app. Will be weird to figure that out but that's something we will figure out at the end.
        
The links of each page are as stated (WHEN HOSTED LOCALLY)
    1.localhost:8000/ (home page)
    2. login/
    3. /
    4. notes/noteview/ (we can also just change this to notes/)
    5. notes/editnote/
    6. calendar/

All of them are literally <p> tags right now.


TODO:
    SET UP USERS/ACCOUNTS AND LOGIN FUNCTIONALITY (ill take care of this) <- i is zach
    SET UP FOLLOWING PAGES:
        SETUP BOOTSTRAP (BIG IMPORTANT WE NEED TO DO THIS EARLY. I WILL DO THIS TMRW UNLESS ONE OF YOU GUYS DOES THIS). This isnt that hard to do, literally copy paste something somewhere but just need to know what we copy paste and where.
        
        Home page
        notes/noteview (again, can just be notes/ i just didnt think of that when i was setting it up)
        notes/editnote
        Calendar page
        Login page (zach doing this)
        
        
    