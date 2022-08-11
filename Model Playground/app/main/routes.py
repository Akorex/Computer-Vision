import os
from flask import render_template, redirect, url_for, request, flash
from app import app
from werkzeug.utils import secure_filename

# utility code
UPLOAD_FOLDER = r".\app\main\uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birds-species', methods=['GET', 'POST'])
def model_birds():
    return render_template('birds.html')

@app.route('/birds-upload', methods=['GET', 'POST'])
def upload_birds():
    if request.method == 'POST':
        #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        f = request.files['file']
        
        # if user does not select file, browser also submit a empty part without filename
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return ""

@app.route('/tumors', methods=['GET', 'POST'])
def model_tumors():
    return render_template('tumors.html')

@app.route('/cats-dogs', methods=['GET', 'POST'])
def model_pets():
    return render_template('pets.html')