# -ECS781P-Group7
<h1 align="center">Cloud Web Application using Python Flask + Background Removal API</h1>
  
<B>ARCHITECTURE</B>
<p align="center">
  <img width="700" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/architecture.jpg" alt="Architecture">
</p>

<B>PRE-REQUISITES</B>
  <br />

To complete this project, you will need the following: 
- Some familiarity with Python. 
- Python installed on a local environment/ cloud environment. 
- Knowledge of Basic Linux Navigation and File Management. 
Here is the file structure of the project once you have completed all the procedures: 
<p align="center">
  <img width="400" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/diagram.jpg" alt="diagram">
</p>

----  
<B>Step 1 — Installing Packages</B>
 <br />
There are three main packages you need for your project: 
- Flask 
- Flask-Login: to handle the user sessions after authentication 
- Flask-SQLAlchemy: to represent the user model and interface with the database You will be using SQLite to avoid having to install any extra dependencies for the database.<br />


First, start with creating the project directory: 
<br />
```diff
mkdir temp_group_project  
```

<br />


Next, navigate to the project directory:
<BR />
```diff
cd temp_group_project 
```

You will want to create a Python environment if you don’t have one. 
In this project, we will use miniconda: 
<BR />
[a link](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)
 
Next, create and activate the environment:
<BR />
```diff
conda create --name group7
conda activate group7
```

This command will activate the virtual environment. 
<BR />
Run the following command from your virtual environment to install the needed packages:
<BR />
```diff
pip install -r requirements.txt 
```
 
Now that you have installed the packages, you are ready to begin.

<b>Step 2 — Creating the Main App File</b>
<BR />
Let’s start by creating a project directory:
<BR />
```diff
mkdir project 
```

The project's _init_.py file:

This file contains the function to create the app, which sets up the database and the blueprints. This is a basic step, but it is essential for the rest of the app. Here, you will initialize SQLAlchemy, configure some settings, and register the blueprints.
<BR />
```diff
nano project/__init__.py 
```
<p align="center">
  <img width="600" src="README\init.png" alt="init">
</p>
 
<b>Step 3 — Adding Routes</b>
<br />
For the main_blueprint, the main blueprint will be used to run the application. First, create main.py:  
```diff
nano main.py 
```

<p align="center">
  <img width="600" src="README\main.png">
</p>

Next, create views.py and auth.py: 
<p align="center">
  <img width="600" src="README\auth.png">
  <img width="600" src="README\views.png">
</p>

<b>Step 4 — Creating Templates </b>
<br />
Next, create the templates that are used in the app. This is the first step before you can implement the actual login functionality. 
<br />
The app will use these templates: 
 - delete.html 
 - images.html 
 - index.html 
 - layout.html
 - login.html 
 - register.html
 - upload.html   
 <br />

	 
---
<b>Step 5 — Creating the Database in the Google Cloud Platform </b>
<br />

Step 5a - Create a New project in the Google Cloud Platform </b>
<br />
<p align="center">
  <img width="600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step5a.png"	
</p>

Step 5b - Select SQL 
<br />
  <p align="center">
 <img width="300" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step5b.png"
</p>
	  
Step 5c - Create an instance for you SQL Database 
<br />
  <p align="center">
 <img width = "600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step5c.png"
</p>
	
Step 5d - Enable the Compute Engine API  
<br />

  <p align="center">
 <img width="600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step5d.png"
</p>
	
Step 5e - Create an instance based on your requirements 
<br />

Your instance requirements will depend on the budget for your project.

  <p align="center">
 <img width="600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step5e.png"
</p>
	
 Step 5f -The My SQL instance has now been created

 <br />
  <p align="center">
 <img width="600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step5f.jpg"
</p>


Step 5g -Create the database in MySQL instance
Click on your instance and go to the left-hand side of the page and click database 

<br />
 <p align="center">
 <img width="600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step5g.png"
</p>

Click on Create database 


Created Database
----
<b>Step 6 — Database Authentication</b>
<br />
To connect to your Google Cloud SQL's database, you need to set up your project. You will need to know your project ID and the name of your database. Execute these commands:

- IAM principal (user, service account, etc.) with the Cloud SQL Client role.
```diff
!gcloud config set project {project_id} 
```

- Enable the Cloud SQL Admin API within your project.
```diff
gcloud projects add-iam-policy-binding {project_id} --member=user:{current_user} --role="roles/cloudsql.client"
```

```diff
gcloud services enable sqladmin.googleapis.com
```

- Create a Cloud SQL instance if it is not already created.
```diff
gcloud sql instances create {instance_name} --database-version=MYSQL_8_0 --region={region} --cpu=1 --memory=4GB --root-password={password} --database-flags=cloudsql_iam_authentication=On
```

- Create a Database
```diff
gcloud sql databases create {db_name} --instance={instance_name}
```

```diff
gcloud sql users create {username} --instance={instance_name} --password="xxxxxxxxxx"
```
You will now see a database created in the Cloud SQL console. 

<b>Step 8 — Creating User Models </b> 

<br /> 

  
A user is represented by a User model. In Flask-SQLAlchemy models are defined using classes. In the figure below we have defined a class called User with the following attributes: id, email, username and password. Each of these attributes is converted to a column in our database. More attributes can be added to your application if this is required, for example data of birth or preferences.   

<br /> 

Models created in Flask-SQLAlchemy are represented by classes that then translate to tables in a database. The attributes of those classes then turn into columns for those tables.  

<br /> 

Create the model.py file for the User model:  

```diff 
nano project/models.py  
```
  

Define the User model:  

  <p align="center"> 

  <img width="600" src=" https://github.com/kienps308/ECS781P-Group7/blob/main/README/step8.jpg "> 

</p> 

We have now established which attributes will be in our database.
<br />

 
<b>Step 9 — Setting Up the external API - remove_bg API </b>
<br />
The background removal functionality is served on the web application from remove.bg, it uses only one API call but an API key is required.
 
HTTP Request in cURL :
```diff
$ curl -H 'X-API-Key: INSERT_YOUR_API_KEY_HERE'           \
       -F 'image_file=@/path/to/file.jpg'                 \
       -F 'size=auto'                                     \
       -f https://api.remove.bg/v1.0/removebg -o no-bg.png
```

A request of the API call will be made if using python, note that the library "requests" is required to be installed. 

Example query:
```diff
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('/path/to/file.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'INSERT_YOUR_API_KEY_HERE'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text) 
```
Let's integrate the request under the *upload_file* function in views.py

<p align="center">
  <img width="600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step7.jpg">
</p>
 

<b>Step 10 — Run the application </b>
<br /> 
Ensure that you are in the flask_cloud_app directory and then run the project: 
<br />
(*Optional*: to activate the debugger for displaying application errors in the browser, set the FLASK_DEBUG environment variable to 1)

```diff
python3 main.py   
``` 
 
Now, in a web browser, you can navigate to the four possible URLs and see the content that was defined in auth.py and views.py. 
 
For example, visiting localhost:5000/ displays: Home: 
 <p align="center">
  <img width="600" src="https://github.com/kienps308/ECS781P-Group7/blob/main/README/step8.jpg">
</p> 

<b>Step 11 — Serving the application over https </b>
<br />
To apply the web app over https, we need a SSL Certificate Files including a ‘key’ file and a ‘cert’, which are the private key file and the certificate file respectively. 
<br /> 
If you don’t have an SSL Certificate, you can generate a self-signed certificate using OpenSSL, to generate a self-signed certificate valid for 10 years, and using the code : 
```diff
req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 3650
```

<br /> 
Then you would be required to input information such as the country name, state name, city name, organisation name, Unit name, common name and email address.

<br/>
After a ‘key’ and ‘cert’ file are generated, implement these files to enable HTTPS and a secure connection, you then need to include them in app.run in the main.py.
<br />
 
```diff
app.run(debug=True, host='0.0.0.0', port = 5000, debug=True, ssl_context=('cert.pem', 'key.pem')) 
```
 <br />

----- 
<b>Conclusion </b>
<br />
We built a login system for an app using Flask-Login and Flask-SQLAlchemy in this app. By initially constructing a user model and saving the user's information, we have demonstrated how to authenticate a user. Then we had to check that the user's password was correct by hashing it and comparing it to the one saved in the database. Finally, we introduced authorisation to the app by using the @login required decorator on a profile page to restrict access to only logged-in users. 
<br />
For simple apps, the code you wrote in this article will suffice, but if you want more functionality right away, you might consider using the Flask-User or Flask-Security libraries, which are both built on Flask. Finally, we have have demonstrated the use of Nasa APOD API to display picture of the day and randomly generated picture of data by passing a random date to the API. 
