from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/') # Equivalent to: app.add_url_rule('/', '', index)
def index():
    return "<h1>Welcome Friend</h1>"

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/api/comic/comicinfo', methods=['POST'])
def comicInfo():
    content_type = request.headers.get('Content-Type')
    print(content_type)

    if content_type == 'application/json':
        content = request.get_json()
        print(content)
        print(content['url'])

    return {"test": "test"}
