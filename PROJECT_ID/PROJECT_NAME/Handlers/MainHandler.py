from PROJECT_NAME.Errors import *
from BaseHandler import *

from peewee import *
from playhouse.db_url import connect

class MainHandler(BaseHandler):
	def get(self):
		self.respond("Welcome to the PROJECT_NAME API.")