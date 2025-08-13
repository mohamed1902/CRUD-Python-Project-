#Model_User
from pydantic import BaseModel
from datetime import datetime

class UserIn(BaseModel):
    name:str
    age:int 
    price:float

class UserOut(UserIn):
    id:str
    create_at:datetime