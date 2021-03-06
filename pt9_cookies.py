from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('cookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
  if request.method == 'POST':
    user = request.form['nm']
   
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)
    print(user)
    return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome ' + str(name) + '</h1>'


if __name__ == '__main__':
   #app.run(debug = True)
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))
  

#Help from:
#https://pythonbasics.org/flask-upload-file/

#https://www.tutorialspoint.com/flask/flask_cookies.htm