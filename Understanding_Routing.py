from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('hello_world.html')


# @app.route('/<endPoint>')
# def routes(endPoint, num=0, name='none', whatever='none'):
#     if endPoint == 'dojo':
#         return render_template('dojo.html')
#     elif endPoint == 'say/<name>':
#         return render_template('say.html', name=name)
#     elif endPoint == 'repeat/<num>/<whatever>':
#         return render_template('repeat.html', num=int(num), whatever=whatever)
#     else:
#         return render_template('error.html', endPoint=endPoint)

@app.route('/dojo')
def dojo():
    return render_template('dojo.html')


@app.route('/say/<name>')
def projects(name):
    return render_template('say.html', name=name)


@app.route('/repeat/<num>/<whatever>')
def contact(num, whatever):
    return render_template('repeat.html', num=int(num), whatever=whatever)


if __name__ == "__main__":
    app.run(debug=True)
