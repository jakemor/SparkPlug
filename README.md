# Spark Plug

A framework for writing RESTful APIs with WebApp2 on Google App Engine in Python with an included helper script to get everything set up. 

## ORM

Peewee. Documentation here.

## Project Structure

/ProjectName
	/project-id 
	/lib
	/ProjectName
		/Handlers
		/Models
		__init__.py
		Errors.py
	/.git
	.gitignore
	app.yaml
	appengine_config.py
	favicon.ico
	index.yaml
	main.py

# Getting Started

1. Create a new project on Google App Engine. Take note of the `project id`. 
2. Create a Cloud SQL Instance on app engine. Take note of the `Instance id` and the `Root password` that you choose during setup. You can chose any location, but I recommend chosing one central to your users. When setup is completed, take note of the `Instance connection name` of your new instance. 
2. Git clone this repository wherever you want your project to live on your machine. Take note of the newly created SparkPlug folder and `cd` into it. 

Structure:

SparkPlug
	/.git
	/PROJECT_ID
	/setup.py
	/README.md


3. Run `python setup.py` and answer all the questions. Don't fuck up, because there's no way to edit yet [you'll need to start over]. You'll notice that the project folder changed from SparkPlug to the name of your project. You'll also notice that the git repository has been deleted.

New Structure:

ProjectName
	/project-id

4. Using the Google App Engine Launcher, go to `File > Add Existing Application` and add the path of the folder named your `project id`. This is not the parent folder, it's the child one. 

5. All set, ensure everything is running and you're good to go =) 