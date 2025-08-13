#Teatchers_Route
from fastapi import APIRouter
from models.modelTeatcher import TeatcherIn , TeatcherOut
from services.serviceTeatcher import create_Teatcher , get_teatchers , update_teatcher , delete_teatcher

router = APIRouter()

@router.post("/", tags=["Table Teatchers"] , response_model=TeatcherOut)
def add_teatcher(teatcher: TeatcherIn):
    return create_Teatcher(teatcher)

@router.get("/", tags=["Table Teatchers"] , response_model=list[TeatcherOut])
def list_teatchers():
    return get_teatchers()

@router.put("/{id}", tags=["Table Teatchers"] , response_model= TeatcherOut)
def updated_teatcher(id: str ,teatcher: TeatcherIn):
    updated = update_teatcher(id, teatcher)
    if updated:
        return updated
    return {"Messeage": "Not Found User"}

@router.delete("/{id}", tags=["Table Teatchers"])
def remove_teatcher(id: str):
    deleted = delete_teatcher(id)
    if deleted:
        return {"Messeage": "Done Delete User"}
    return {"Messeage": "Not Found User"}