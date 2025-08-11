#Users_Services
from models.modelUser import User , request_user , userOut
from sqlalchemy.orm import session
from datetime import datetime

def create_user(user: request_user , db:session):
    new_user =  User(name=user.name , age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return userOut(id=new_user.id , name=new_user.name , age=new_user.age , time=new_user.time)

def get_users(db: session):
    users = db.query(User).all()
    return [userOut(id=u.id, name=u.name, age=u.age, time=u.time) for u in users]

def update_user(id: int,user: request_user, db: session):
    ex_user = db.query(User).filter(User.id == id).first()
    if not ex_user:
        return None
    ex_user.name = user.name
    ex_user.age = user.age
    ex_user.time = datetime.now()
    db.commit()
    db.refresh(ex_user)
    return userOut(id=ex_user.id , name=ex_user.name , age=ex_user.age , time=ex_user.time)

def delete_user(id: int, db: session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user