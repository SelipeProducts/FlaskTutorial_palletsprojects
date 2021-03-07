#Note: copy code from pt files and paste it into main to run

#Book Notes:
import random
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index_flash.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'secret': error = 'Invalid credentials'
        
    else:
      flash('You were successfully logged in')
      return redirect(url_for('index'))
  return render_template('login_flash.html', error=error)

if __name__ == '__main__':
   #app.run(debug = True)
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))
