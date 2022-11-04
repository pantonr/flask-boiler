from flask import Flask, render_template
import win32api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/do_something')
def do_something():
  """
  Do something on button press.
  """
  # your code
  win32api.MessageBox(0, 'hello', 'title')
  return res





if __name__ == '__main__': app.run(debug=True)