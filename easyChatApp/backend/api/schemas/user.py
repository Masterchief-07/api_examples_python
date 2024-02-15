from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id:int
    nom:str
    numero:str
    model_config=ConfigDict(from_attributes=True)

class CreateUser(BaseModel):
    nom:str
    numero:str
    password:str
    model_config=ConfigDict(from_attributes=True)

class ModifyUser(BaseModel):
    nom:str|None
    numero:str|None
    password:str|None
    model_config=ConfigDict(from_attributes=True)
