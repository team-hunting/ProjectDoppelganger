This repo automatically deploys to https://hip-flask.herokuapp.com/ <br/>

To develop against repo effectively, turn on Debug/Development mode. <br/>
Run the command: "export FLASK_ENV=development", then use "flask run" in the same directory as wsgi.py. Because our entry point is named "wsgi.py" (this is a special name in flask) we don't need to set the FLASK_APP environment variable. "app.py" works as well. <br/>
This enables hot reloading and a traceback console in the browser.

Windows Powershell: $env:FLASK_ENV = "development"  <br/>
Windows Git Bash:   export FLASK_ENV=development <br/>
Windows CMD:        set FLASK_ENV=development <br/>
Linux/etc:          export FLASK_ENV=development <br/>

Please note that you will need to update requirements.txt with any new requirements for Heroku.<br/>

The WSGI server gives off a warning saying "WARNING: This is a development server. Do not use it in a production deployment." if you run it without 'development' mode on. On heroku we run using Gunicorn instead. This is controlled with the Procfile.<br/>

Note: HTTP response 304 is for "Redirection to a previously cached result".