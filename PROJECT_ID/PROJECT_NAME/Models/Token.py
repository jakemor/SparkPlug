from BaseModel import *
from User import *
import uuid

class Token(BaseModel):

	user = ForeignKeyField(User, related_name='UserTokens')

	def serializable(self):
		return {
			"Type": "Token",
			"Authorization": self.id.hex
		} 