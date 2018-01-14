from BaseModel import *
from User import *
import uuid

class Token(BaseModel):

	user = ForeignKeyField(User, related_name='UserTokens')

	def serializable(self):
		return {
			"type": "Token",
			"value": self.id.hex
			"time_created": self.to_timestamp(self.time_created),
			"time_last_modified": self.to_timestamp(self.time_last_modified),
		} 