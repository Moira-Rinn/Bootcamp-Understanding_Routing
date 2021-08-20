from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hello_world.html')


@app.route('/dojo')
def about():
    return render_template('dojo.html')


@app.route('/say/<name>')
def projects(name):
    if type(name) == int:
        return render_template('say.html', name=name)
    else:
        return render_template('error.html', name=name)


@app.route('/repeat/<num>/<whatever>')
def contact(num, whatever):
    return render_template('repeat.html', num=int(num), whatever=whatever)


if __name__ == "__main__":
    app.run(debug=True)
