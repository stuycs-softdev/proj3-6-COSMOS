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

def getName(name):  
    list = db.info.find_one( {"owner":name}, fields = {"_id_":False})
    return list["owner"]
    
def getHealth(pname):
    list = db.info.find_one( {"name":pname}, fields = {"_id_":False})
    return list["health"]
    
def getHunger(pname):
    list = db.info.find_one( {"name":pname}, fields = {"_id_":False})
    return list["hunger"]
    
def getClean(pname):
    list = db.info.find_one( {"name":pname}, fields = {"_id_":False})
    return list["cleanliness"]

def getHappiness(pname):
    list = db.info.find_one( {"name":pname}, fields = {"_id_":False})
    return list["happiness"]

def updateHealth(pname):
    
    
def updateHunger(pname):
    
    
def updateClean(pname):
    
    
def updateHappiness(pname):
