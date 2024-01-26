from flask import render_template, redirect, url_for, request, jsonify
from . import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/members')
def members():
    members_data = [
            {"name": "Jason", "age": "27"},
            {"name": "Alice", "age": "25"}
        ]

    return render_template('members.html', members = members_data)