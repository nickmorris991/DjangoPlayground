# purpose
note: this is a continuation of many basic django tutorials

- learn the django project layout
- improve python web skillset
- prepare for production grade django work / codebase
 

# notes 

## Documentation of Running Knowledge

### basic commands
- python manage.py runserver (spin up local server at port :8000)
- python manage.py migrate (update the connected backend server with most recent models)

### basic layout
- similiar to mvc layout each landing page has its own directory where you can adjust models.py, views.py, etc
- use urls.py in each subdirectory for url mapping
    - note: you can pass variables between endpoints through the mapping process
    - after hitting a subdirectories urls.py page it's passed to the views page by giving it a route, view, and possibly name