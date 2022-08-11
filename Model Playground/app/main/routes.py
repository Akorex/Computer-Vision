from flask import render_template
from app import app

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birds-species')
def model_birds():
    return render_template('birds.html')

@app.route('/tumors')
def model_tumors():
    return render_template('tumors.html')

@app.route('/cats-dogs')
def model_pets():
    return render_template('pets.html')