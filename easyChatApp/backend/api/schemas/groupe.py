from pydantic import BaseModel, ConfigDict
from api.schemas.user import User

class CreateGroupe(BaseModel):
    title:str
    description:str

    model_config=ConfigDict(from_attributes=True)

class ModifyGroupe(BaseModel):
    title:str|None
    description:str|None
    model_config=ConfigDict(from_attributes=True)

class Groupe(BaseModel):
    id:int
    title:str
    description:str
    created_by:int
    model_config=ConfigDict(from_attributes=True)

class GroupeWithUser(BaseModel):
    id:int
    title:str
    description:str
    created_by:User
    model_config=ConfigDict(from_attributes=True)
