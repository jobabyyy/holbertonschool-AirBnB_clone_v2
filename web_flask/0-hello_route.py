#!/usr/bin/python3
<<<<<<< HEAD
"""Starting Flask web application"""

=======
"""Starting Flast web application"""
>>>>>>> b215705d9fd07f2073d1b8578473a537994f4b34
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
