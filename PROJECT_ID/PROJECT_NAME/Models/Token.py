from BaseModel import *
from User import *
import uuid

class Token(BaseModel):
	id = UUIDField(primary_key=True)
	user = ForeignKeyField(User, related_name='UserTokens')

	def serializable(self):
		return {
			"Type": "Token",
			"Authorization": self.id.hex
		} 