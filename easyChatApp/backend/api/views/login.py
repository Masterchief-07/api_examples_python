from typing import Annotated
from fastapi import APIRouter, Depends, Form
from api.database import Session, get_db
from api.services import login as loginSvc
from api.schemas.response import Response

login_router = APIRouter()

@login_router.post("/", response_model=Response[str])
async def login(
    number:Annotated[str, Form()],
    password:Annotated[str, Form()],
    db:Session = Depends(get_db)
):
    token = loginSvc.login(
        number=number,
        password=password, 
        db=db)
    
    return Response(
        message=token
    )