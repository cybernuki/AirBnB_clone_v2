#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    res = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, result=res)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    states = storage.all("State")
    if id:
        states = states.get('State.{}'.format(id), None)
    return render_template('9-states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
