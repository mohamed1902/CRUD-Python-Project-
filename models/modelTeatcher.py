#model_Teatcher
from pydantic import BaseModel
from datetime import datetime

class TeatcherIn(BaseModel):
    name: str
    age: int

class TeatcherOut(TeatcherIn):
    id:str
    create_at:datetime
    