#!/usr/bin/python3
"""
Starts a Flask web application

"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    returns Hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    display “C ” followed by the value
    of the text variable replacing underscore
    _ symbols with a space
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    display “Python ”, followed by the value
    of the text variable replacing underscore _
    symbols with a space
    """

    return 'Python {}'.format(text.replace('_',' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Displays 'n is a number' only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    """
    Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_even(n):
    """
    Returns HTML page only if n is integer
    """
    desc = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, desc=desc)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
