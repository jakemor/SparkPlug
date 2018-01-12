from PROJECT_NAME.Errors import *
from PROJECT_NAME.Models.User import *
from BaseHandler import *

from peewee import *
from playhouse.db_url import connect

# MainHandler

class TokenHandler(BaseHandler):

	# TODO: Document

	def post(self):

		# check for params

		try: 

			# get payload

			post = self.get_params()

			# assert params

			self.assert_params(post, ["email", "password"])

			# get the user

			user = User.get(User.email == post["email"])

			# verify the password

			user.verify_password(post["password"])

			# create the token

			key = Token(id = uuid.uuid4())
			key.user = user

			key.save(force_insert=True)

			self.respond(key.serializable())


		except Exception as e:
			
			self.error(e)


	def get(self):
		
		try: 

			# get the user
			user = User().from_token(self.token())

			self.respond("Hello %s. Your request is valid. Happy coding!" % user.username)
		
		except Exception as e:
			self.error(e)	

	def put(self):
		self.error(NotFoundException())

	def delete(self):
		
		try: 

			# get the user
			user = User().from_token(self.token())

			deleteQuery = Token.delete().where(Token.user == user)

			record_affected = deleteQuery.execute()

			self.respond({"tokens_deleted": record_affected})
		
		except Exception as e:
			
			self.error(e)

