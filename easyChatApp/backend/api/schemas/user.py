from pydantic import BaseModel

class User(BaseModel):
    id:int
    nom:str
    numero:str

class CreateUser(BaseModel):
    nom:str
    numero:str
    password:str

class ModifyUser(BaseModel):
    nom:str|None
    numero:str|None
    password:str|None
