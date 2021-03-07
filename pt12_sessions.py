
from flask import Flask, session, redirect, url_for, request
from markupsafe import escape
import random


app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


#-------------------------------------------------
#My Cat Version
@app.route('/cat')
def cat():
    if 'cat' in session:
        return 'Your favorite type of cat is %s' % escape(session['cat'])
    return 'You do not have a favorite cat...'

@app.route('/cat_select', methods=['GET', 'POST'])
def cat_select():
    if request.method == 'POST':
        session['cat'] = request.form['cat']
        return redirect(url_for('cat'))
    return '''
      <form method="post">
        <label for="cats">Choose a car:</label>
          <select id="cats" name="cat">
            <option value="stay">Stray</option>
            <option value="fluffy">Fluffy</option>
            <option value="bald">Bald</option>
            <option value="black">Black</option>
          </select>
          <p><input type=submit value=Select>
      </form>
    '''

if __name__ == '__main__':
   #app.run(debug = True)
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))
