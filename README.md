# Github_Repos

## For Backend Task:
 *I use postman to test all endpoints*
1 - The endpoint to list the languages used by the 100 trending public repos on GitHub
http://127.0.0.1:8000/repos/languages 

2 - The endpoint for displaying number of repos using language and list these repos 
  http://127.0.0.1:8000/repos/languages/<language> by replacing <language> with
  any language to search about it.
  
  
## For Frontend Task:
  This is a link to show all repos created in the last 30 days (relative to 2017-11-22)
    http://127.0.0.1:8000/repos/
    
    
## To run this project
- clone the project.

- create and start a a virtual environment.
   " virtualenv env --no-site-packages "
   " source env/bin/activate "
   
- Install all dependencies.
  " pip install -r requirements.txt "

- cd into the project's home directory.

- run server
  " python manage.py runserver "
