
## Dev Info:

To develop Flask apps more effectively, turn on Debug/Development mode. <br/>
Run the command: ```export FLASK_ENV=development```, then use "flask run" in the same directory as wsgi.py (or just run wsgi.py). Because our entry point is named "wsgi.py" (this is a special name in flask) we don't need to set the FLASK_APP environment variable. "app.py" works as well. <br/>
This enables hot reloading and a traceback console in the browser.

Windows Powershell: ```$env:FLASK_ENV = "development"```  <br/>
Windows Git Bash:   ```export FLASK_ENV=development```    <br/>
Windows CMD:        ```set FLASK_ENV=development```       <br/>
Linux/etc:          ```export FLASK_ENV=development```    <br/>

Please note that you will need to update requirements.txt with any new requirements for Heroku.<br/>

If you run the app without development mode on, the WSGI server gives off a warning saying "WARNING: This is a development server. Do not use it in a production deployment." On Heroku we wrap the app with Gunicorn to support concurrency. This is controlled with the Procfile.<br/>

On Heroku WEB_CONCURRENCY config variable is set to 3 as per https://devcenter.heroku.com/articles/python-gunicorn <br/>

You will need to set a ```MONGODB_URI``` environment variable to connect to the DB. The value (for this specific deployment) can be found in the heroku settings if you have access. <br/>

## Notes:

HTML Escaping / Sanitizing inputs: <br/>
```
from markupsafe import escape
... return f"Hello, {escape(name)}!"
```

Templates rendered with Jinja will escape user values automatically. <br/>

Note: HTTP response 304 is for "Redirection to a previously cached result". <br/>

Flask quickstart: https://flask.palletsprojects.com/en/2.0.x/quickstart/ <br/>

Bootstrap components: https://getbootstrap.com/docs/5.0/customize/components/ <br/> 

Client Side zip & download functionality is contained under static/utilities/zip <br/>
