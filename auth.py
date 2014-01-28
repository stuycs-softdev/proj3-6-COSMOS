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
        
        
def newPet(pname):
    if (db.info.find( {"name":pname} )).count() > 0:
        return False
    else:
        return True

<<<<<<< HEAD
def getName(pname):  
    return pet["name"]
    
=======
def getName(name):  
    list = db.info.find_one( {"owner":name}, fields = {"_id_":False})
    return list["owner"]
>>>>>>> 2f932b5a2bf31962abad43b9dff51a381eb1dc17
    
def getHealth(pname):
    return pet["health"]
    

def getHunger(pname):
    return pet["hunger"]
    
def getClean(pname):
    return pet["cleanliness"]

def getHappiness(pname):
<<<<<<< HEAD
    return pet["happiness"]
=======
    list = db.info.find_one( {"name":pname}, fields = {"_id_":False})
    return list["happiness"]

def updateHealth(pname):
    
    
def updateHunger(pname):
    
    
def updateClean(pname):
    
    
def updateHappiness(pname):
>>>>>>> 2f932b5a2bf31962abad43b9dff51a381eb1dc17
