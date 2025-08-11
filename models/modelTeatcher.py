#model_Teatcher
from pydantic import BaseModel
from datetime import datetime
from pgAdmin.Connection import Base
from sqlalchemy import Column ,  Integer , String , DateTime

class Teatcher(Base):
    __tablename__ = "teatchers"

    id = Column(Integer , primary_key=True , nullable=False)
    name =  Column(String , nullable=False)
    age = Column(Integer, nullable=False)
    time = Column(DateTime , default=datetime.utcnow)

class request_teatcher(BaseModel):
    name: str
    age: int

class teatcherOut(request_teatcher):
    id:int
    time: datetime
    class config:
        orm_mode= True