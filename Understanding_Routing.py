from flask import Flask, render_template
from flask.globals import request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hello_world.html')


@app.route('/dojo')
def dojo():
    return render_template('dojo.html')


@app.route('/say/<name>')
def say(name):
    return render_template('say.html', name=str(name))


@app.route('/repeat/<num>/<whatever>')
def repeat(num, whatever):
    return render_template('repeat.html', num=int(num), whatever=whatever)


if __name__ == "__main__":
    app.run(debug=True)
