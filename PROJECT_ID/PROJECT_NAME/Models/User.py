import hashlib, uuid

from BaseModel import *
from PROJECT_NAME.Errors import *

class User(BaseModel):
	
	name = CharField(max_length=50, default="")
	email = CharField(max_length=50, unique=True)
	username = CharField(max_length=50, unique=True)
	avatar_url = CharField(max_length=255, default="")
	cover_url = CharField(max_length=255, default="")
	bio = CharField(max_length=500, default="")
	
	password_hash = CharField(max_length=255)


	def from_token(self, token):
		from Token import *
		try:
			return Token.get(Token.id == token).user
		except Exception as e:
			e.message = "Invalid token in authorization header"
			raise e

	def set_password(self, password):

		salt = uuid.uuid4().hex
		p = ''.join([salt, "jm@#4nEy123#@%".encode("utf-8") ,password.encode("utf-8")])
		m = hashlib.md5() 
		m.update(p)
		self.password_hash = '.'.join([salt, m.hexdigest()])

	def verify_password(self, password):

		parts = self.password_hash.split(".")
		salt = parts[0]
		p = ''.join([salt, "jm@#4nEy123#@%".encode("utf-8") ,password.encode("utf-8")])
		m = hashlib.md5() 
		m.update(p)

		if m.hexdigest() != parts[1]:
			e = UnauthorizedException()
			e.message = "Incorrect Password"
			raise e

	def serializable(self): 
		return {
			"type": "User",
			"id": self.id.hex,
			"time_created": self.to_timestamp(self.time_created),
			"time_last_modified": self.to_timestamp(self.time_last_modified),
			"name": self.name,
			"email": self.email,
			"avatar_url": self.avatar_url,
			"cover_url": self.cover_url,
			"bio": self.bio,
		} 
