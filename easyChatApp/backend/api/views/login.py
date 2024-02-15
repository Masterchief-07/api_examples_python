from fastapi import APIRouter, Depends
from api.database import Session, get_db
from api.services import login as loginSvc

login_router = APIRouter()

@login_router.post("/")
async def login(
    number:str,
    password:str,
    db:Session = Depends(get_db)
):
    token = loginSvc.login(
        number=number,
        password=password, 
        db=db)
    
    return token