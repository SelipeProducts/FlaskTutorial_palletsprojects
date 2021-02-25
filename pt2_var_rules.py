#var rule converter and trailing slash

from flask import Flask
import random
#used in converter section
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

#add variable sections to a URL by marking sections with <variable_name>. 
#Your function then receives the <variable_name> as a keyword argument.


#CAN USE CONVERTERS to pass vars to URL 
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

#Trailing slash
#if route ends with / it is a directery
  #directories will redirect route with / is it is forgotten
#if route ends with path. It is a file
  #if / is included at the end of a file. A 404 error ocurs
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


if __name__ == "__main__":
    # app.run(host, port)
    app.run(
        host='0.0.0.0',
        port=random.randint(2000, 9000))

#Converter types:
  # string (default) - accepts any text without a slash
  # int - accepts positive integers
  # float - accepts positive floating point values
  # path - like string but also accepts slashes
  # uuid - accepts UUID strings