#Model_User
from pydantic import BaseModel
from datetime import datetime
from pgAdmin.Connection import Base
from sqlalchemy import Column , Integer , String , DateTime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer , primary_key=True , nullable=False)
    name = Column(String , nullable=False)
    age = Column(Integer , nullable=False)
    time = Column(DateTime , default=datetime.utcnow)
class request_user(BaseModel):
    name: str 
    age: int 

class userOut(request_user):
    id: int 
    time: datetime

    class config:
        orm_mode = True