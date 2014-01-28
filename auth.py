import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.database
users = db.users
pets = db.pets
     
def register(user, pword):
    if((users.find( {"username":user} ))).count() > 0:
        return False
    elif ( (users.find({"password":pword}) ) ).count() > 0:
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
    if ((pets.find({'owner':user}))).count() > 0:
        return True
    else:
        return False
        
def newPet(pname, oname):
    if (pets.find( {"name":pname}, {"owner":oname} )).count() > 0:
        return False
    else:
        pets.insert( {"owner": oname},
                     {"name":pname},
                     {"health":100},
                     {"hunger":100},
                     {"hygiene":100},
                     {"happiness":100} )
        users.update(
            {"username":oname},
            {"$inc": {"players.pets":1}}
            ) 
        return True    


def getOwner(pname):  
    pet = pets.find_one( {"name":pname}, fields = {"_id":True})
    return pet["owner"]
    
def getHealth(pname):
    pet = pets.find_one( {"name":pname}, fields = {"_id":True})
    return pet["health"]
    
def getHunger(pname):
    pet = pets.find_one( {"name":pname}, fields = {"_id":True})
    return pet["hunger"]
    
def getHygiene(pname):
    pet = pets.find_one( {"name":pname}, fields = {"_id":True})
    return pet["hygiene"]

def getHappiness(pname):
    pet = pets.find_one( {"name":pname}, fields = {"_id":True})
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
