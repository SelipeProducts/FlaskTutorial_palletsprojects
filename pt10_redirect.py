from flask import Flask, abort, redirect, url_for,  render_template, make_response
import random

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

def this_is_never_executed():
  print("Check check check. Is this executed?")

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
    return "hi"

#how to handle the error
@app.errorhandler(401)
def page_not_found(error):
    return render_template('page_not_found.html'), 401

# you want to get hold of the resulting response object inside the view you can use the make_response()

# just need to wrap the return expression with make_response() and get the response object to modify it, then return it:

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

if __name__ == '__main__':
   #app.run(debug = True)
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))

