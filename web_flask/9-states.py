#!/usr/bin/python3
"""states"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page of all State objects present in DBStorage"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page of City objects linked to a State object"""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    else:
        cities = state.cities if type(storage).__name__ == 'DBStorage' \
                 else state.cities()
        return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
