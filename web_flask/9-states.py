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

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Routes:
    /states/<id>: display a HTML page: (inside the tag BODY)
    If a State object is found with this id:
    H1 tag: "State: "
    H3 tag: "Cities:"
    UL tag: with the list of City objects linked
    to the State sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
    H1 tag: "Not found!"
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
