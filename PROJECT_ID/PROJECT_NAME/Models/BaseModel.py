import os, datetime, operator, hashlib
from peewee import *
from playhouse.db_url import connect
from datetime import date
from time import mktime
from time import strftime

dev = os.environ['SERVER_SOFTWARE'].startswith('Development')

if dev:	
	# local
	print "[*] -- LOCAL DEVELOPMENT"
	db = connect("mysql://root:root@127.0.0.1:3306/PROJECT_NAME")
else:
	# server
	print "[*] -- SERVER DEVELOPMENT"
	db = connect(os.environ.get('DATABASE'))


	
class BaseModel(Model):

	id = UUIDField(primary_key=True)
	time_created = DateTimeField(default=datetime.datetime.now)
	time_last_modified = DateTimeField(default=datetime.datetime.now)
	
	class Meta:
		database = db

	def to_timestamp(self, date):
		return mktime(date.timetuple())

	def from_timestamp(self, time):
		return datetime.datetime.fromtimestamp(int(time))

	def update_time_last_modified(self):
		if hasattr(self, "time_last_modified"):
			setattr(self, "time_last_modified", datetime.datetime.now())

	def set_values(self, values, variables):
		
		for var in variables:
			if var in values:		
				if hasattr(self, var) and var != "password_hash":
					if var == "id" or var == "time_created":
						continue
					
					if getattr(self, var) != values[var]:	
						setattr(self, var, values[var])
						self.update_time_last_modified()
				
				elif var == "password":
					self.set_password(values[var])
					self.update_time_last_modified()

				else:
					e = BadRequestException()
					e.message = "'%s' is not an acceptable value" % (var)

	@classmethod
	def matching_params(Table, values, variables, match_and = True):

		if len(values.keys()) == 0:
			return

		clauses = []
		order_by = Table.time_created
		limit = None
		offset = None

		standard_variables = ["order_by", "descending", "desc", "limit", "offset", "organization"]

		# add standard variables if needed

		for var in standard_variables:
			if var not in variables:
				variables.append(var)

		for var in variables:
			if var in values:
				
				# order by	

				if var == "order_by":
					order_by = getattr(Table, values[var])
					continue

				# desc

				if (var == "desc" or var == "descending"):
					order_by = order_by.desc()
					continue

				# limit

				if var == "limit": 
					limit = int(values[var])
					continue

				# offset

				if var == "offest": 
					offset = int(values[var])
					continue

				if hasattr(Table, var):
					clauses.append((getattr(Table, var) % values[var]))


		rows = Table.select().where(reduce(operator.and_, clauses)).order_by(order_by)

		if limit:
			rows = rows.limit(limit)

		if offset:
			rows = rows.offset(offset)


		objects = []

		for r in rows:
			objects.append(r.serializable())


		return objects


