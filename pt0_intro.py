#Most Basic Flask App
import random

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, World!'

if __name__ == '__main__':
  #app.run(debug=True)    #Note: Debug mode not working on repl.it
  
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))

# 1) Imported the Flask class. 

# 2) Create an instance of this class. The first argument is the name of the application’s module or package. This is needed so Flask knows where to look for templates, static files, etc.

# 3) Use the route() decorator to tell Flask what URL should trigger our function.

# 4) The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.


#-------------------------------------------------------
#To run the application you can either use the flask command or python’s -m switch with Flask. 

#Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable:

      # $ export FLASK_APP=hello.py
      # $ flask run
      #   * Running on http://127.0.0.1:5000/

#####     On Windows
#   C:\path\to\app>set FLASK_APP=hello.py

#####     alternative

#     $ export FLASK_APP=hello.py
#     $ python -m flask run
#        * Running on http://127.0.0.1:5000/




#-------------------------------------


#In case the python -m flask fails or flask does not exist, there are multiple reasons this might be the case.

#Old Version of Flask

#Invalid Import Name

#---------------------------------------------------
#Debug Module

# $ export (set[on windows]) FLASK_ENV=development
# $ flask run


#does the following things:
#1)it activates the debugger
#2)it activates the automatic reloader
#3)it enables the debug mode on the Flask application.