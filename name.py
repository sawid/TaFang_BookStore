import datetime
from database import DB
class Name(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.created_at = datetime.datetime.utcnow()
        
    def insert(self):
            result_temp = DB.insertName(collection='user_db', data=self.json())
            if result_temp == "Can Login":
                    return "Succcess"
            elif result_temp == "Cannot Login":
                    return "Failed"
            elif result_temp == "Register":
                    print("Name Regis") 
                    return "Regist Success"

    def json(self):
        return {
           'username': self.name,
           'password': self.password,
           'created_at': self.created_at
        }