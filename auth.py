import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.database
users = db.users
pets = db.pets
     
def register(user, pword):
    if((users.find( {"username":user} ))).count() > 0:
        return False
    
    else:
        users.insert( {"username":user, "password":pword, "pets": 0} )
        return True
    
def authenticate(user, pword):
    if ((users.find( {"username":user}, {"password":pword} ))).count() > 0:
        return True
    else:
        return False
        
def hasPet(user):
    if ((pets.find( {"owner":user}))).count > 0:
        return True
    else:
        return False
        
def newPet(pname, oname):
    if (pets.find( {"name":pname}, {"owner":oname} )).count() > 0:
        return False
    else:
        pets.insert( {
                "owner":oname,
                "name":pname,
                "health":100,
                "hunger":100,
                "hygiene":100,
                "happiness":100 } )
        users.update(
            {"username":oname},
            {"$inc": {"players.pets":1}}
            ) 
        return True    

def getPet(user):
    pet =  pets.find_one({'owner':user})
    return pet["name"]

def getOwner(pname):  
    pet = pets.find_one( {"name":pname}, fields = {"_id":True})
    return pet["owner"]

def getHealth(pname):
    ph=  pets.find( {"name":pname}, {"health":1, "_id":0} )
    return ph[0]['health']
            
def getHunger(pname):
    ph=  pets.find( {"name":pname}, {"hunger":1, "_id":0} )
    return ph[0]['hunger']
    
def getHygiene(pname):
    ph=  pets.find( {"name":pname}, {"hygiene":1, "_id":0} )
    return ph[0]['hygiene']
    
def getHappiness(pname):
    ph=  pets.find( {"name":pname}, {"happiness":1, "_id":0} )
    return ph[0]['happiness']
    
def updateName(pname,newName):
    pets.update(
        {"name": pname },
        { "$set": {'name':newName} }
        )

def updateHealth(pname,newHealth):
    pets.update(
        { "name": pname },
        { "$set": {'health': newHealth} }
        )

def decHunger(pname):
    pets.update(
        { "name": pname},
        { "$inc": {'hunger': -10} }
        )

def incHygiene(pname):
    pets.update(
        { "name": pname},
        { "$inc": {'hygiene': 10} }
        )
    
def incHappiness(pname):
    pets.update(
        { "name": pname},
        { "$inc": {'happiness': 10} }
)
