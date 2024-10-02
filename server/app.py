#!/usr/bin/env python3

from flask import Flask # type: ignore

app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# Define a dynamic route for user profiles
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Ensure the Flask app runs when the script is executed
if __name__ == '__main__':
    app.run(port=5555, debug=True)
