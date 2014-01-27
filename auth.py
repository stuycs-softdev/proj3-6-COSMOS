import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.users
collection = db.info

def register(user, pword):
    if((db.info.find( {"username":user}, fields={"_id":False} ))).count() > 0:
        return False
    else:
        db.info.insert( {"username":user, "password":pword} )
        return True
    
def authenticate(user, pword):
    if ((db.info.find( {"username":user}, {"password":pword} ))).count() > 0:
        return True
    else:
        return False
