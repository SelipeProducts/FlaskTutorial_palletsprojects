from flask import Flask
import random

app = Flask(__name__)

# route() decorator to bind a function to a URL.
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=random.randint(2000, 9000))