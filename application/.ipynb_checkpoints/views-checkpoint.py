import os
from flask import Blueprint, redirect, render_template, request
from flask_login import login_required,current_user
from application import app

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
UPLOAD_FOLDER = './uploads'
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
    """
    Uploads a file to the server.

    Parameters:
        None

    Returns:
        - If the file is successfully uploaded, returns a string "File uploaded successfully".
        - If the file is invalid or the upload fails, returns a string "Invalid file format".
    """
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

    '''maybe the remove_bg.py can be added here'''
    
    """
    Returns:
        - If the file is successfully uploaded, returns the output result (image_w/o_bg).
        - If the file is invalid or the upload fails, returns a string "Invalid file format".
        """