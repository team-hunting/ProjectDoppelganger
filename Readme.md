This repo automatically deploys to https://hip-flask.herokuapp.com/ <br/>

To run this app locally, you run wsgi.py <br/>

Please note that you will need to update requirements.txt with any new requirements (pretty sure Heroku needs it) <br/>

The WSGI server gives off a warning saying "WARNING: This is a development server. Do not use it in a production deployment." We can replace it with something like 'waitress' once the app is production ready <br/>

Note: HTTP response 304 is for "Redirection to a previously cached result".