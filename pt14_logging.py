from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def log():
  app.logger.debug('A value for debugging')
  app.logger.warning('A warning occurred (%d apples)', 69)
  app.logger.error('An error occurred')
  return "logger"

if __name__ == '__main__':
   #app.run(debug = True)
  app.debug = True
  app.run(host='0.0.0.0',
  port=random.randint(2000, 9000))