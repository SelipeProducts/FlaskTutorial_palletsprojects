#Note: copy code from pt files and paste it into main to run

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
# import random
# from flask import request, Flask

# app = Flask(__name__)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/static/uploaded_file.txt')
#         #f.save('/var/www/uploads/uploaded_file.txt')


# if __name__ == '__main__':
#   app.debug = True
#   app.run(host='0.0.0.0',
#   port=random.randint(2000, 9000))
import random
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(f.filename)
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   #app.run(debug = True)
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))


#Got code from:  https://pythonbasics.org/flask-upload-file/