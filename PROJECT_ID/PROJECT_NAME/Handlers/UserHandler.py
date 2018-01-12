import uuid


from PROJECT_NAME.Errors import *
from BaseHandler import *

from peewee import *
from playhouse.db_url import connect

class UserHandler(BaseHandler):

	""" 
	
	Create a User

	"""

	def post(self, search = None):

		if search:
			self.get()
			return

		try: 

			# get post body

			post = self.get_params()

			# check parameters

			self.assert_params(post, ["email", "username", "password"])

			# create the user 

			user = User(id = uuid.uuid4())
			user.set_values(post, ["name", "email", "username", "password", "bio"])
			user.save(force_insert=True)

			# respond with the user

			self.respond(user.serializable())


		except Exception as e:

			self.error(e)
			return

	def put(self):
		
		try: 
			
			# get post body
		
			post = self.get_params()
			
			# verify token, get active org
			
			user = User().from_token(self.token())
		
			# update new fields

			user.set_values(post, ["name", "email", "username", "password", "bio"])
		
			# save the admin
			
			user.save()

			self.respond(user.serializable())

		except Exception as e:

			self.error(e)
			return

	def get(self, user_id=None, search=None):

		try: 
			
			user = User().from_token(self.token())
			
			if user_id: # get single user

				# get the user

				user = User.get(User.id == user_id)

				# respond with single user

				self.respond(user.serializable())

			else: # searching for users
				
				# get the params

				get = self.get_params()

				# get the admins

				users = User.matching_params(get, ["name", "email", "username",])

				# respond with the admins

				self.respond(users)
			

		except Exception as e:
			self.error(e)
			return
		
	def delete(self, admin_id):
		
		try: 
			
			user = User().from_token(self.token())

			user.delete_instance()

			self.respond()

		except Exception as e:
			self.error(e)
			return
		