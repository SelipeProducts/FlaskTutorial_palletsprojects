from flask import Flask, request, render_template

app = Flask(__name__)

#By default, a route only answers to GET requests. 
#You can use the methods argument of the route() decorator to handle different HTTP methods.
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username, password):
  pass

def log_the_user_in(username):
  pass

#------------------------------------------------------
#render a template you can use the render_template() method. 
#All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments


#------------------------------------------------------

#Get

#GET is used to request data from a specified resource.
#Note that the query string (name/value pairs) is sent in the URL of a GET request:


#ex) /test/demo_form.php?name1=value1&name2=value2

# GET requests can be cached
# GET requests remain in the browser history
# GET requests can be bookmarked
# GET requests should never be used when dealing with sensitive data
# GET requests have length restrictions
# GET requests are only used to request data (not modify)

#Post

# POST is used to send data to a server to create/update a resource.

# The data sent to the server with POST is stored in the request body of the HTTP request:

#ex) POST /test/demo_form.php HTTP/1.1
#    Host: w3schools.com
#    name1=value1&name2=value2

# POST requests are never cached
# POST requests do not remain in the browser history
# POST requests cannot be bookmarked
# POST requests have no restrictions on data length
