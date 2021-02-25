from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

    #Check line 36 for details
    print(url_for('static', filename='style.css'))

#Use the url_for() function to build a URL to a specific function
#Function accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule

# test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell



#-------------------------------------------------------

#Static Files Building


#Dynamic web applications also need static files. That’s usually where the CSS and JavaScript files are coming from. Ideally your web server is configured to serve them for you, but during development Flask can do that as well. 

#Just create a folder called static in your package or next to your module and it will be available at /static on the application.

#To generate URLs for static files, use the special 'static' endpoint name:

def static_file_url_builder():
  url_for('static', filename='style.css')


