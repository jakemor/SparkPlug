import shutil, os, fnmatch

print """

  __,                    _ __  _       
 (                    / ( /  )//       
  `.   ,_   __,  _   /<  /--'// , , _, 
(___)_/|_)_(_/(_/ (_/ |_/   (/_(_/_(_)_
      /|                            /| 
     (/                            (/  

https://github.com/jakemor/SparkPlug

Welcome! Please answer the questions below. 
If you fuck up, delete this folder and git clone again.
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
	("PROJECT_NAME", "What is your project name?"),
	("PROJECT_ID", "What is your project id?"),
	("SQL_PROD_USER","What is the user's username on your production sql isntance?"),
	("SQL_PROD_PASS","What is the user's password on your production sql isntance?"),
	("SQL_IP_ADDRESS","What is the sql instance's IP address?"),
	("SQL_INSTANCE_ID","What is the 'Instance id' of your sql instance?"),
	("SQL_INSTANCE_CONNECTION_NAME","What is the 'Instance connection name' of your sql instance?")
]

# rename folders and variables
for q in questions:
	keyName = q[0]
	question = q[1]

	keyValue = raw_input(question + " ")

	findReplace(PROJECT_DIRECTORY, keyName, keyValue, "*.py")
	findReplace(PROJECT_DIRECTORY, keyName, keyValue, "*.yaml")

findReplace(PROJECT_DIRECTORY, 'SPARKPLUG_GITIGNORE', '.gitignore', '*')

# rename parent folder

# delete readme
os.remove('README.md')

# delete .git
shutil.rmtree('.git')

# delete setup.py
os.remove('setup.py')




