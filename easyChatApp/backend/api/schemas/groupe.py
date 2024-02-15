from pydantic import BaseModel
from api.schemas.user import User

class CreateGroupe(BaseModel):
    title:str
    description:str

class ModifyGroupe(BaseModel):
    title:str|None
    description:str|None

class Groupe(BaseModel):
    id:int
    title:str
    description:str
    created_by:int

class GroupeWithUser(BaseModel):
    id:int
    title:str
    description:str
    created_by:User