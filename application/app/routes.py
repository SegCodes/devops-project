from flask import flash, render_template, redirect, url_for, request, jsonify
from . import app

@app.route('/')
def home():
    return render_template('home.html')