from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome Friend</h1>"

@app.route('/test')
def test():
    return render_template('test.html')