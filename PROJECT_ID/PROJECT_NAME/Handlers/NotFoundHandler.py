from PROJECT_NAME.Errors import *
from BaseHandler import *

from peewee import *
from playhouse.db_url import connect

class NotFoundHandler(BaseHandler):
	def post(self, page):
		self.error(NotFoundException())

	def get(self, page):
		self.error(NotFoundException())

	def put(self, page):
		self.error(NotFoundException())

	def delete(self, page):
		self.error(NotFoundException())