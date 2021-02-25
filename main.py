#import pt0_intro

# from flask import Flask, request, render_template
# import random

# app = Flask(__name__,template_folder='templates',
#     static_folder='static')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# def do_the_login():
#   random_num = random.randint(1, 100000)

#   return render_template('login.html', random_number=random_num)

# def show_the_login_form():
#   print("yes")
#   pass

# #By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.

# if __name__ == "__main__":
#     # app.run(host, port)
#     app.run(  # Starts the site
#         # EStablishes the host, required for repl to detect the site
#         host='0.0.0.0',
#         # Randomly select the port the machine hosts on.
#         port=random.randint(2000, 9000))


#----------------------------------------

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

#Use the url_for() function to build a URL to a specific function
#Function accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule

# test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell