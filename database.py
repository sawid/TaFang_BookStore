import pymongo
class DB(object):
     URI = "mongodb://127.0.0.1:27017"
     
     @staticmethod
     def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['list-user']

     @staticmethod
     def insertName(collection, data):
        temp_username = data["username"]
        temp_password = data["password"]
        print(data["username"])
        check_temp_num = DB.DATABASE[collection].find({'username': temp_username})
        if check_temp_num.count() > 0:
                print("More Than 1")
                for result_object in check_temp_num:
                        print(result_object)
                        if result_object['password'] == temp_password:
                                print("Can Login")
                        else:
                                print("Cant Login") 
        else:
                DB.DATABASE[collection].insert(data)

     @staticmethod
     def listName(collection, query):
        return DB.DATABASE[collection].find()