# Run this code locally
- Clone repo: ```git clone https://github.com/team-hunting/ProjectDoppelganger.git```
- cd into repo: ```cd ProjectDoppelganger```
- Create python virtual env: ```python -m venv venv```
- Activate venv: ```venv/Scripts/activate```
- Install requirements: ```pip install -r requirements.txt```
- Run app: ```flask run```
- Good to go! Navigate to ```http://127.0.0.1:5000/``` in a web browser.
- Note: I like to modify the activate script and add the line ```set FLASK_ENV=development``` (this is for windows - other OS specific commands listed below)

# Integrating with Vue
- Add 'build' parameters to the vite.config.ts file in your Vue app (under the resolve parameter) ```build: {outDir: "./dist", assetsDir: 'static'}```
- Set Flask to serve out of these folders: ```app = Flask(__name__, static_folder='./dist/static', template_folder='./dist')```
- Build your vue app with ```npm run build```
- Copy over the newly created 'dist' folder into your Flask directory - under the 'app' folder
- Copy anything from your Flask 'templates' folder into 'dist'
- Copy anything from your Flask 'static' folder into 'dist/static'

# Docker
https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ <br/>
https://medium.com/swlh/how-to-use-docker-images-containers-and-dockerfiles-39e4e8fc181a <br/>

Build the docker image with the name flask-doppelganger ```docker build --tag flask-doppelganger .```  <br/>
Create the docker container using the flask-doppelganger image (using port 5000) ```docker create --name flaskd --init -p 5000:5000 flask-doppelganger``` <br/>
View the created container ```docker ps -a --filter "name=flaskd"``` <br/>
Start the container (App now accessible on http://localhost:5000/) ```docker start flaskd``` <br/>
View running containers ```docker ps``` <br/>
View logs for the running container ```docker logs -f flaskd``` <br/>
Open interactive bash shell to explore the running container (-it for interactive) ```docker exec -it flaskd bash``` <br/>

Stop container ```docker stop flaskd``` <br/>
Remove container ```docker rm flaskd``` <br/>

Stop ALL running containers ```docker stop $(docker ps -q)``` <br/>

The run command creates, starts, and attaches a docker container (-d starts the container in detached mode, --rm removes the container from the machine when it is stopped) (App now accessible on http://localhost:5000/)```docker run -d --name flaskd -p 5000:5000 --init --rm flask-doppelganger``` <br/>

View all docker images on your machine ```docker image ls``` <br/>

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
