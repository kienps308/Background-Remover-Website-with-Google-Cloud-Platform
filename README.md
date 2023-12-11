# -ECS781P-Group7

Step 1: install the required packages:
pip install -r requirements.txt
Step 2: run the following command:
flask run

--------Revise the documentation below--------
<h1 align="center">Cloud Web Application using Python Flask + Background Removal API</h1>
  
<B>ARCHITECTURE</B>
<p align="center">
  <img width="700" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/architecture.jpg" alt="Architecture">
</p>

<B>PRE-REQUISITES</B>
  <br />

To complete this project, you will need the following: 
- Some familiarity with Python. 
- Python installed on a local environment/ cloud environment. 
- Knowledge of Basic Linux Navigation and File Management. 
Here is a diagram to provide a sense of what the file structure of the project will look like once you have completed the tutorial: 
 <p align="center">
  <img width="400" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/files.jpg" alt="Architecture">
</p>
  
<B>Step 1 — Installing Packages</B>
 <br />
There are three main packages you need for your project: 
- Flask 
- Flask-Login: to handle the user sessions after authentication 
- Flask-SQLAlchemy: to represent the user model and interface with the database You will be using SQLite to avoid having to install any extra dependencies for the database.<br />


First, start with creating the project directory: 
<br />
```diff
mkdir cloud_flask_app  
```
<br />


Next, navigate to the project directory:
<BR />
```diff
cd cloud_flask_app 
```

You will want to create a Python environment if you don’t have one. 
Depending on how Python was installed on your machine, your command will look like: 
<BR />
```diff
sudo apt-get install python3-venv 
Python3 -m venv nasa 
```
 	
The -m flag is for module-name. This command will execute the module venv to create a new virtual environment named nasa. This will create a new directory containing bin, include, and lib subdirectories. And a pyvenv.cfg file. 
 
Next, run the following command:
<BR />
```diff
source nasa/bin/activate 
```
This command will activate the virtual environment. 
Run the following command from your virtual environment to install the needed packages:
<BR />
```diff
nano requirements.txt  
```
	 
copy paste the contents of requirement.txt files and save. 
<BR />
```diff
pip install -r requirements.txt 
```
 
Now that you have installed the packages, you are ready to create the app. 

<b>Step 2 — Creating the Main App File</b>
<BR />
Let’s start by creating a project directory:
<BR />
```diff
mkdir project 
```
The first file will be the __init__.py file for the project: 

This file will have the function to create the app, which will initialize the database and register the blueprints. Now, this will not do much, but it will be needed for the rest of the app. You will need to initialize SQLAlchemy, set some configuration values, and register the blueprints here: 
<BR />
```diff
nano project/__init__.py 
```
 <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step2.jpg" alt="Architecture">
</p>
 

<b>Step 3 — Adding Routes</b>
<br />
For the main_blueprint, the main blueprint will be used to run the application. First, create main.py:  
```diff
nano main.py 
```
<p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/Step3.jpg">
</p>

Next, create views.py: 
For the routes, you will use two blueprints. 
For the views_blueprint, you will have a home page (/) and a profile page (/profile). 
```diff
nano project/views.py
```
<p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step3-1.jpg">
</p>

For the auth_blueprint, you will have routes to retrieve both the login page (/login) and the sign-up page (/signup). Finally, you will have a logout route (/logout) to log out an active user. Next, create auth.py: 
<br />
```diff
nano project/auth.py 
```
Then add your auth_blueprint: 
<p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step3-2.jpg">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step3-3.jpg">
</p>

<b>Step 4 — Creating Templates </b>
<br />
Next, create the templates that are used in the app. This is the first step before you can implement the actual login functionality. 
<br />
The app will use four templates: 
 - index.html 
 - profile.html 
 - login.html 
 - signup.html 
 <br />
 
You will also have a base template that will have code common to each of the pages. 
<br />
In this case, the base template will have navigation links and the general layout of the page. 
First, create a templates directory under the project directory: 
```diff
mkdir -p project/templates
```
Then create base.html: 
```diff
nano project/templates/base.html 
```

Next, add the following code to the base.html file: 
<p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step4.png">
</p>
 
 
 
This code will create a series of menu links to each page of the application. It also establishes a block for content that can be overwritten by child templates. 
Next, create templates/index.html: 
```diff
nano project/templates/index.html 
```
 
Add the following code to the newly created file to add content to the page:  
 <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step4-1.jpg">
</p>
   
This code will create a basic index page with a title and subtitle. 
 
Next, create templates/login.html: 
```diff
nano project/templates/login.html  
```

This code generates a login page with fields for Email and Password. There is also a checkbox to “remember” a logged in session. 
 <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step4-2.jpg">
</p>
 
Next, create templates/signup.html: 
```diff
nano project/templates/signup.html  
```
 
Add the following code to create a sign-up page with fields for email, name, and password: 
 <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step4-3.jpg">
</p>
  
 
Next, create templates/profile.html: 
```diff
nano project/templates/profile.html  
```
 
This is where we will display the data fetched for the NASA APOD API 
 <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step4-4.jpg">
</p>
 	 

<b>Step 5 — Creating User Models </b>
<br />
The user model represents what it means for the app to have a user. This tutorial will require fields for an email address, password, and name. In future applications, you may decide you want much more information to be stored per user. You can add things like birthdays, profile pictures, locations, or any user preferences. 
<br />
Models created in Flask-SQLAlchemy are represented by classes that then translate to tables in a database. The attributes of those classes then turn into columns for those tables. 
<br />
Create the User model: 
```diff
nano project/models.py 
```
 	
Define the User model: 
  <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step5.jpg">
</p>
  
 
This code defines a User with columns for an id, email, password, and name. 
Now that you’ve created a User model, you can move on to configuring your database. 
<br />

<b>Step 6 — Configuring the Database </b>
<br />
You will be using an SQLite database. You could create an SQLite database on your own, but let’s have Flask-SQLAlchemy do it for you. You already have the path of the database specified in the __init__.py file, so you will need to tell Flask-SQLAlchemy to create the database in the Python REPL. 
<br />
Ensure that you are still in the virtual environment and in the flask_cloud_app directory. 
If you stop your app and open a Python REPL, you can create the database using the create_all method on the db object: 
```diff
python  
from project import db, create_app, models  	
db.create_all(app=create_app())  	
exit()  
```
You will now see a db.sqlite file in your project directory. This database will have the user table in it. 
 
<b>Step 7 — Setting Up the JavaScript for fetching data from Nasa APOD API </b>
<br />
One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. 
 
HTTP Request :
```diff
GET https://api.nasa.gov/planetary/apod  
```

concept_tags are now disabled in this service. Also, an optional return parameter copyright is returned if the image is not public domain. 
  <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step7.jpg">
</p>
 
Example query :
```diff
https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY   
```
<p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step7-1.jpg">
</p>
 

<b>Step 8 — Run the application </b>
<br />
The FLASK_DEBUG environment variable is enabled by setting it to 1. This will enable a debugger that will display application errors in the browser. 
<br /> 
Ensure that you are in the flask_cloud_app directory and then run the project: 
```diff
python3 main.py   
```
 
           
 
Now, in a web browser, you can navigate to the five possible URLs and see the text returned that was defined in auth.py and views.py. 
 
For example, visiting localhost:5000/ displays: Home: 
 <p align="center">
  <img width="600" src="https://github.com/karanpardeshi11/Nasa/blob/main/ReadMe/step8.jpg">
</p> 
 	 
 
<b>Conclusion </b>
<br />
We built a login system for an app using Flask-Login and Flask-SQLAlchemy in this app. By initially constructing a user model and saving the user's information, we have demonstrated how to authenticate a user. Then we had to check that the user's password was correct by hashing it and comparing it to the one saved in the database. Finally, we introduced authorisation to the app by using the @login required decorator on a profile page to restrict access to only logged-in users. 
<br />
For simple apps, the code you wrote in this article will suffice, but if you want more functionality right away, you might consider using the Flask-User or Flask-Security libraries, which are both built on Flask. Finally, we have have demonstrated the use of Nasa APOD API to display picture of the day and randomly generated picture of data by passing a random date to the API. 
