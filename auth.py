import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.users
collection = db.info
pets = db.pets
pet = db.info.find_one( {"name":pname}, fields = {"_id_":False})
    
def register(user, pword):
    if((collection.find( {"username":user}, fields={"_id":False} ))).count() > 0:
        return False
    else:
        collection.insert( {"username":user, "password":pword} )
        return True
    
def authenticate(user, pword):
    if ((collection.find( {"username":user}, {"password":pword} ))).count() > 0:
        return True
    else:
        return False

def getName(pname):  
    return pet["name"]
    
    
def getHealth(pname):
    return pet["health"]
    

def getHunger(pname):
    return pet["hunger"]
    
def getClean(pname):
    return pet["cleanliness"]

def getHappiness(pname):
    return pet["happiness"]
