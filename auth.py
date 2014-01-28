import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.database
users = db.user

pets = db.pets
pet = pets.find_one( {"name":pname}, fields = {"_id":True})
    
def register(user, pword):
    if((users.find( {"username":user}, fields={"_id":True} ))).count() > 0:
        return False
    else:
        users.insert( {"username":user, "password":pword} )
        return True
    
def authenticate(user, pword):
    if ((users.find( {"username":user}, {"password":pword} ))).count() > 0:
        return True
    else:
        return False
        
        
def newPet(pname, oname):
    if (pets.find( {"name":pname} )).count() > 0:
        return False
    else:
        pets.insert( {"owner": oname}, {"name":pname}, {"health":100}, {"hunger":100}, {"hygiene":100}, {"happiness":100} )
        return True    


def getName(name):  
    return pet["owner"]
    
def getHealth(pname):
    return pet["health"]
    
def getHunger(pname):
    return pet["hunger"]
    
def getClean(pname):
    return pet["cleanliness"]

def getHappiness(pname):
    return pet["happiness"]

def updateHealth(pname,newHealth):
    pets.update(
        { "_id": ObjectId(document_id) },
        { "$set": {'health': newHealth} }
        )

    
def updateHunger(pname,newHunger):
    pets.update(
        { "_id":ObjectId(document_id) },
        { "$set": {'hunger': newHunger} }
        )

def updateHygiene(pname,newHygiene):
    pets.update(
        {"_id":ObjectId(document_id) },
        { "$set": {'hygiene': newHygiene} }
        )
    
def updateHappiness(pname,newHappiness):
    pets.update(
        {"_id":ObjectId(document_id) },
        { "$set": {'happiness': newHappiness} }
)
