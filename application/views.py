import os, sys, requests, time
from flask import Blueprint, redirect, render_template, request
from flask_login import login_required,current_user

from flask import Flask, render_template, url_for

from application import app
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)
imageData = [{"imageID":"1111","title":"something.jpg","description":"Something something","Created date":"30/08/2000"}]

@views.route('/')
@views.route('/index')
@views.route('/home')
def index():
    return render_template('index.html')


@views.route('/images')
@login_required
def images():               
    """
    Render the "images.html" template with the provided `imageData` and `images` variables.
    
    :return: The rendered HTML page.
    """
    return render_template("images.html", imageData=imageData, images = True, name=current_user.name)



@views.route('/delete', methods=['GET','POST']) 
def delete():
    """
    Delete function for handling the '/delete' route.

    Parameters:
    - None

    Returns:
    - delete.html: A rendered template for the 'delete.html' file.
    - delete: A boolean indicating that the delete operation was successful.
    - data: A dictionary containing the 'imageID', 'title', and 'description' of the deleted item.
    """
    imageID = request.form.get('imageID')
    title = request.form.get('title')
    description = request.form.get('description')
    return render_template('delete.html', delete = True, data = {"imageID":imageID, "title":title, "description":description})

# Configure the upload folder
UPLOAD_FOLDER = 'application/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Function to check if a file has an allowed extension
def allowed_file(filename):
    """
    Check if a file is allowed based on its extension.

    Parameters:
        filename (str): The name of the file to be checked.

    Returns:
        bool: True if the file is allowed, False otherwise.
    """
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@views.route('/upload', methods=['GET'])
@login_required
def upload():
    """
    Renders the 'upload.html' template with the 'upload' variable set to True.

    :return: The rendered HTML page.
    """
    return render_template('upload.html', upload = True)

@views.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        #print(file_path)
        
        #file_path2 = 'application/static/images/'+filename
        #print(filename)
        
        new_fpath = None
        
        #remember to register the API key on the website
        #one API key can only test 50 times, or will be charged the fee
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(file_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'n2bbL2GRd5vmejYKyr8yLdC7'},
        )
        
        if response.status_code == requests.codes.ok:
            new_filename = 'nobg_'+os.path.splitext(filename)[0]+'.png'
            new_fpath = 'application/static/images/'+new_filename
            print(new_fpath)
            with open(new_fpath, 'wb') as out:
                out.write(response.content)
            
        else:
            print("Error:", response.status_code, response.text)
            
        return render_template('upload.html', image_url=new_filename)
    else:
        return "Invalid file format. Allowed formats are jpg, jpeg, png, and gif."