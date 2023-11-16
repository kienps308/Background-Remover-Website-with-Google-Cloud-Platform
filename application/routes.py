import os
from application import app
from flask import Response, json, redirect, render_template, request


imageData = [{"imageID":"1111","title":"something.jpg","description":"Something something","Created date":"30/08/2000"}]

# Define a route and its corresponding function
@app.route('/')))
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', index = True )

@app.route('/login')
def login():
    return render_template('login.html', login = True )

@app.route('/images')
def images():               
    return render_template("images.html", imageData=imageData, images = True )

@app.route('/register')
def register():
    return render_template('register.html', register = True )

@app.route('/delete', methods=['GET','POST']) 
def delete():
    imageID = request.form.get('imageID')
    title = request.form.get('title')
    description = request.form.get('description')
    return render_template('delete.html', delete = True, data = {"imageID":imageID, "title":title, "description":description})

# Configure the upload folder
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Function to check if a file has an allowed extension
def allowed_file(filename):
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions
@app.route('/upload', methods=['GET'])
def upload():
 return render_template('upload.html', upload = True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully'
    return 'Invalid file format'
