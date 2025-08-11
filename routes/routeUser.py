#Users_Route
from fastapi import APIRouter ,Depends 
from sqlalchemy.orm import session
from models.modelUser import User , request_user , userOut
from services.serviceUser import create_user , get_users , update_user , delete_user
from pgAdmin.Connection import get_db

router = APIRouter()

@router.post("/", tags=["Table Users"] , response_model=userOut)
def add_user(user: request_user, db: session = Depends(get_db)):
    return create_user(user, db)

@router.get("/" , tags=["Table Users"] , response_model=list[userOut])
def list_users(db : session = Depends(get_db)):
    return get_users(db)

@router.put("/{id}", tags=["Table Users"] , response_model=userOut)
def updated_user(id: int ,user: request_user, db:session = Depends(get_db)):
    updated = update_user(id, user, db)
    if updated:
        return updated
    return {"Messeage": "Not Found User"}

@router.delete("/{id}", tags=["Table Users"])
def remove_user(id: int ,db: session= Depends(get_db)):
    deleted = delete_user(id , db)
    if deleted:
        return {"Messeage": "Done Delete User"}
    return {"Messeage": "Not Found User"}