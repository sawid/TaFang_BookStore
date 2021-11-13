import datetime
from database import DB
class Name(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.created_at = datetime.datetime.utcnow()

    def insert(self):
            DB.insertName(collection='user_db', data=self.json())

    def json(self):
        return {
           'username': self.name,
           'password': self.password,
           'created_at': self.created_at
        }