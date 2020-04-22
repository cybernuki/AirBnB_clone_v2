#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def state_list():
    states = storage.all("State")
    amaneties = storage.all("Amenity")

    return render_template('10-hbnb_filters.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
