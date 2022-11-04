from flask import Flask, render_template


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
  return "Hello, Welcome to GeeksForGeeks"






if __name__ == '__main__': app.run(debug=True)