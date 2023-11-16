import os
from application import app
from flask import Response, json, redirect, render_template, request, session
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR

imageData = [{"imageID":"1111","title":"something.jpg","description":"Something something","Created date":"30/08/2000"}]

# Define a route and its corresponding function
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    """
    A function that serves as the route handler for the homepage.

    Returns:
        The rendered index.html template with the index variable set to True.
    """
    return render_template('index.html', index = True)

@app.route('/login', methods=['GET','POST'] )
def login():
    """
    A decorator that specifies the route '/login' for the login function.

    Returns:
        The rendered template 'login.html' with the login variable set to True.
    """
    if request.method == 'POST':
        user = request.form['username']
        session['username'] = user
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect('/images')
    else: 
        return render_template('login.html', login = True )

@app.route('/images')
def images():               
    """
    Render the "images.html" template with the provided `imageData` and `images` variables.
    
    :return: The rendered HTML page.
    """
    return render_template("images.html", imageData=imageData, images = True )

@app.route('/register')
def register():
    """
    A description of the register function.

    This function is the route handler for the '/register' URL. It renders the 'register.html'
    template and passes the value True to the 'register' variable in the template context.

    Returns:
        The rendered 'register.html' template.

    """
    return render_template('register.html', register = True )

@app.route('/delete', methods=['GET','POST']) 
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

@app.route('/upload', methods=['GET'])
def upload():
    """
    Renders the 'upload.html' template with the 'upload' variable set to True.

    :return: The rendered HTML page.
    """
    return render_template('upload.html', upload = True)

@app.route('/upload', methods=['POST'])
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
