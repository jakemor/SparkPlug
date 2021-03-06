#!/usr/bin/env python
import shutil, os, fnmatch, sys

print """

       __,                    _ __  _       
      (                    / ( /  )//       
       `.   ,_   __,  _   /<  /--'// , , _, 
     (___)_/|_)_(_/(_/ (_/ |_/   (/_(_/_(_)_
           /|                            /| 
          (/                            (/  
 
 
     https://github.com/jakemor/SparkPlug
 
     If you fuck up while answering the questions,
     delete this folder and git clone again.
 

     Before starting: 

 
  1  Create a new project in Google Cloud Platform], 
     then set up App Engine within that project. Take 
     note of the name you chose as well as the 'project
     id'. 
 
  2  Create a Cloud SQL Instance within the project as
     well. Take note of the 'instance id' and the 
     'root password' that you choose during setup. When
     setup is completed, take note of the 'instance
     connection name' of your new instance. 
 
  3  When you see that setup is complete, click on the
     instance id, and go to Databases. Create a new
     database and name it the same as your project. in
     step one.
 
  4  Lastly, authorize your current network in the 
     Authorization section so you can connect to the 
     instance locally. 

"""

def findReplace(directory, find, replace, filePattern, testing=False):
  for path, dirs, files in os.walk(os.path.abspath(directory)): 
    for filename in fnmatch.filter(files, filePattern):
      filepath = os.path.join(path, filename)
      
      if (not testing):
        with open(filepath) as f:
          s = f.read()
        s = s.replace(find, replace)
        with open(filepath, "w") as f:
          f.write(s)
    for i in range(len(dirs)):
      newname = dirs[i].replace(find, replace)
      os.rename(os.path.join(path, dirs[i]), os.path.join(path, newname))
      dirs[i] = newname

PROJECT_DIRECTORY = ''

questions = [
  ("a", "What is your project name?"),
  ("a", "What is your project id?"),
  ("a","What is the user's username on your production sql isntance?"),
  ("a","What is the user's password on your production sql isntance?"),
  ("","What is the sql instance's IP address?"),
  ("a","What is the 'Instance id' of your sql instance?"),
  ("a","What is the 'Instance connection name' of your sql instance?")
]

answers = []

# rename folders and variables
for q in questions:
  keyName = q[0]
  question = q[1]

  keyValue = raw_input("     " + question + " ")

  answers.append((keyName, keyValue))

answer = ""

while not (answer.lower() == "yes" or answer.lower() == "y" or answer.lower() == "n" or answer.lower() == "no"):
  answer = raw_input("     Are all the above fields correct? (Y/n) ")

if (answer.lower() == "n" or answer.lower() == "no"):
  print """
     Alrighty then, aborting.
  """
  sys.exit(0)

for a in answers:
  findReplace(PROJECT_DIRECTORY, a[0], a[1], "*.py")
  findReplace(PROJECT_DIRECTORY, a[0], a[1], "*.yaml")


# delete readme
# os.remove('README.md')

# delete .git
# shutil.rmtree('.git')

# delete setup.py
# os.remove('setup.py')

print """
     Setup Complete.                      

     Next, rename your .gitignore file, initialize a
     new git repository and add the child folder to
     GoogleAppEngineLauncher.
 
     =)

"""




