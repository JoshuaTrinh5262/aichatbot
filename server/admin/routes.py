from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask-Admin!'
    
@app.route('/test')
def test():
    return 'test page, Flask-Admin!'