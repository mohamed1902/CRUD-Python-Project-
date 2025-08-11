#Teatchers_Route
from fastapi import APIRouter , Depends
from sqlalchemy.orm import session
from models.modelTeatcher import Teatcher , request_teatcher , teatcherOut
from services.serviceTeatcher import create_Teatcher , get_teatchers , update_teatcher , delete_teatcher
from pgAdmin.Connection import get_db

router = APIRouter()

@router.post("/", tags=["Table Teatchers"] , response_model=teatcherOut)
def add_teatcher(teatcher: request_teatcher,db: session = Depends(get_db)):
    return create_Teatcher(teatcher , db)

@router.get("/", tags=["Table Teatchers"] , response_model=list[teatcherOut])
def list_teatchers(db: session = Depends(get_db)):
    return get_teatchers(db)

@router.put("/{id}", tags=["Table Teatchers"] , response_model= teatcherOut)
def updated_teatcher(id: int ,teatcher: request_teatcher, db:session = Depends(get_db)):
    updated = update_teatcher(id, teatcher, db)
    if updated:
        return updated
    return {"Messeage": "Not Found User"}

@router.delete("/{id}", tags=["Table Teatchers"])
def remove_teatcher(id: int ,db: session= Depends(get_db)):
    deleted = delete_teatcher(id , db)
    if deleted:
        return {"Messeage": "Done Delete User"}
    return {"Messeage": "Not Found User"}