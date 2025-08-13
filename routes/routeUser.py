#Users_Route
from fastapi import APIRouter
from models.modelUser import UserIn , UserOut
from services.serviceUser import create_user , get_users , update_user , delete_user

router = APIRouter()

@router.post("/", tags=["Table Users"] , response_model=UserOut)
def add_user(user: UserIn):
    return create_user(user)

@router.get("/" , tags=["Table Users"] , response_model=list[UserOut])
def list_users():
    return get_users()

@router.put("/{id}", tags=["Table Users"] , response_model=UserOut)
def updated_user(id: str ,user: UserIn):
    updated = update_user(id, user)
    if updated:
        return updated
    return {"Messeage": "Not Found User"}

@router.delete("/{id}", tags=["Table Users"])
def remove_user(id: str):
    deleted = delete_user(id)
    if deleted:
        return {"Messeage": "Done Delete User"}
    return {"Messeage": "Not Found User"}