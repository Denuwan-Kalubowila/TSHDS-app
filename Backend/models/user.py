from pydantic import BaseModel,EmailStr
from datetime import datetime

class User(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    telephone:str
    city:str
    created_at:datetime
    updatated_at:datetime
