"""
This script runs the Selectel application using a development server.
"""

from os import environ
from Selectel import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    PORT=5000
    app.run(HOST, PORT)
