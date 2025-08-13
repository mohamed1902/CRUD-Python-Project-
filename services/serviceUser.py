#Users_Services
from models.modelUser import UserIn , UserOut
from datetime import datetime
from bson import ObjectId
from database.Connection import mongo

collection_user = mongo.get_collection("user")

def create_user(user: UserIn) -> UserOut:
    user_data = user.dict()
    user_data["create_at"] = datetime.utcnow()
    result = collection_user.insert_one(user_data)
    new_user = collection_user.find_one({"_id": result.inserted_id})
    return UserOut(id=str(new_user["_id"]), **{k: v for k,v in new_user.items() if k != "_id"})

def get_users() -> list[UserOut]:
    return [UserOut(id=str(u["_id"]), **{k: v for k, v in u.items() if k != "_id"})
            for u in collection_user.find()]

def update_user(user_id: str,user: UserIn) -> UserOut:
    collection_user.update_one({"_id": ObjectId(user_id)}, {"$set":{**user.dict(), "create_at":datetime.utcnow()}})
    updatedUser = collection_user.find_one({"_id": ObjectId(user_id)})
    if updatedUser:
        return UserOut(id=str(updatedUser["_id"]),**{k: v for k,v in updatedUser.items() if k !="_id"})

def delete_user(user_id: str) -> bool:
    result = collection_user.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0