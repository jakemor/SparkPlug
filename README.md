# SparkPlug

A framework for writing RESTful APIs with WebApp2 on Google App Engine in Python with out of the box support for user management, and an included helper script to get everything set up. 

## Project Structure
```
/ProjectName
  /project-id 
  /lib
  /ProjectName
    /Handlers
    /Models
    __init__.py
    Errors.py
  /.git
  Rename me to .gitignore
  app.yaml
  appengine_config.py
  favicon.ico
  index.yaml
  main.py
```

## Documentation

Coming soon! For now, try to figure it out! 

## ORM

[Peewee](http://fill.in). Documentation [here](http://fill.in).

# Getting Started

Assuming you've built many apps on app engine and google cloud platform, this should be pretty self explanitory! If you need help, shoot me an email. 

## Setting up Google Cloud Platform

1. Create a new project in [Google Cloud Platform](http://fill.in), then set up App Engine within that project. Take note of the `Project id`. 
2. Create a Cloud SQL Instance within the project as well. Take note of the `Instance id` and the `Root password` that you choose during setup. You can chose any location, but I recommend chosing one central to your users. When setup is completed, take note of the `Instance connection name` of your new instance. 
3. When you see that setup is complete, click on the instance id, and go to Databases. Create a new database and name it the name of your project.
4. Next go to Authorization and add your home network so you can connect to the database from home. 

##  Setting up MySQL on your local Machine

1. Make sure you have Google App Engine launcher installed on your machine, with the python 2.7 runtime. 
2. Download and install a program like [MAMP](http://fill.in) to run a MySQL server locally.
3. Install an SQL browser, like [Sequel Pro](http://fill.in) (included in MAMP).
4. Create a new database locally, and name it the name of your Project
5. Make sure the user and password are both root (important!). 

## Setting up SparkPlug locally 

1. Git clone this repository wherever you want your project to live on your machine. Take note of the newly created SparkPlug folder and `cd` into it. 

Structure:
```
SparkPlug
  /.git
  /PROJECT_ID
  /setup.py
  /README.md
```

2. Run `python setup.py` and answer all the questions. Don't fuck up, because there's no way to edit yet [you'll need to start over]. You'll notice that the project folder changed from SparkPlug to the name of your project. You'll also notice that the git repository has been deleted.

New Structure:
```
SparkPlug
  /project-id
```

3. Rename the `SpakPlug` directory to your project name, then using the Google App Engine Launcher, go to `File > Add Existing Application` and add the path of the folder named your `project id`. This is not the parent folder, it's the child one. 

4. Rename the .gitignore file, initialize a `git` repo in the child folder and you're good to go =). 

# Fin

That's it! If you need any help feel free to shoot me an email. jakemny@gmail.com. 