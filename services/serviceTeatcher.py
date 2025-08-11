#Teatcher_Services
from models.modelTeatcher import Teatcher , request_teatcher , teatcherOut
from sqlalchemy.orm import session
from datetime import datetime

def create_Teatcher(teatcher: request_teatcher , db:session):
    new_teatcher =  Teatcher(name=teatcher.name , age=teatcher.age)
    db.add(new_teatcher)
    db.commit()
    db.refresh(new_teatcher)
    return teatcherOut(id=new_teatcher.id , name=new_teatcher.name , age=new_teatcher.age , time=new_teatcher.time)

def get_teatchers(db: session):
    users = db.query(Teatcher).all()
    return[teatcherOut(id=u.id , name=u.name , age=u.age , time=u.time) for u in users]

def update_teatcher(id: int,teatcher: request_teatcher, db: session):
    ex_teatcher = db.query(Teatcher).filter(Teatcher.id == id).first()
    if not ex_teatcher:
        return None
    ex_teatcher.name = teatcher.name
    ex_teatcher.age = teatcher.age
    ex_teatcher.time = datetime.now()
    db.commit()
    db.refresh(ex_teatcher)
    return  teatcherOut(id=ex_teatcher.id, name=ex_teatcher.name, age=ex_teatcher.age, time=ex_teatcher.time)

def delete_teatcher(id: int, db: session):
    teatcher = db.query(Teatcher).filter(Teatcher.id == id).first()
    if not teatcher:
        return None
    db.delete(teatcher)
    db.commit()
    return teatcher