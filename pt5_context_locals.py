from flask import request, Flask

#Certain objects in Flask are global objects that work as proxies to objects that are local to a specific context. Enables Multithreading

#This is useful when unit testing

app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


#Alternative passing a whole WSGI environment to the request_context() method

#with app.request_context(environ):
#    assert request.method == 'POST'

#To access parameters submitted in the URL (?key=value)
def get_url_parameter():
  searchword = request.args.get('key', '')

  return searchword




