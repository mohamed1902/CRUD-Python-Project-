#Teatcher_Services
from models.modelTeatcher import TeatcherIn , TeatcherOut
from datetime import datetime
from bson import ObjectId
from database.Connection import mongo

collection_teatcher = mongo.get_collection("teatcher")

def create_Teatcher(teatcher: TeatcherIn) -> TeatcherOut:
    teatcher_data = teatcher.dict()
    teatcher_data["create_at"] = datetime.utcnow()
    result = collection_teatcher.insert_one(teatcher_data)
    new_teatcher = collection_teatcher.find_one({"_id": result.inserted_id})
    return TeatcherOut(id=str(new_teatcher["_id"]), **{k: v for k,v in new_teatcher.items() if k != "_id"})

def get_teatchers() -> list[TeatcherOut]:
    return [TeatcherOut(id=str(u["_id"]), **{k: v for k, v in u.items() if k != "_id"})
            for u in collection_teatcher.find()]

def update_teatcher(teatcher_id:str , teatcher: TeatcherIn) -> TeatcherOut:
    collection_teatcher.update_one({"_id": ObjectId(teatcher_id)}, {"$set":{**teatcher.dict() , "create_at": datetime.utcnow()}})
    updatedTeatcher = collection_teatcher.find_one({"_id": ObjectId(teatcher_id)})
    if updatedTeatcher:
        return  TeatcherOut(id=str(updatedTeatcher["_id"]),**{k: v for k,v in updatedTeatcher.items() if k !="_id"})

def delete_teatcher(teatcher_id: str) -> bool:
    result = collection_teatcher.delete_one({"_id": ObjectId(teatcher_id)})
    return result.deleted_count > 0