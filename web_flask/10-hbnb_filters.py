#!/usr/bin/python3
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page like 6-index.html,
    which was done during the project 0x01.
    AirBnB clone - Web static
    """
    all_states = []
    all_amenities = []
    states = storage.all('State')
    amenities = storage.all('Amenity')
    for state in states.values():
        all_states.append(state)
    for amenity in amenities.values():
        all_amenities.append(amenity)
    all_states = sorted(all_states, key=lambda k: k.name)
    all_amenities = sorted(all_amenities, key=lambda k: k.name)
    return render_template('10-hbnb_filters.html',
                           states=all_states, amenities=all_amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
