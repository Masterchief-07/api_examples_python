from fastapi import APIRouter, Depends, HTTPException
from api.services import (
    user as usersvc
)
from api.database import get_db
from api.schemas.response import Response

user_router = APIRouter()

@user_router.get("/")
async def get_User():
    pass

@user_router.post("/", response_model=Response[usersvc.userSch.User])
async def create_user(
    info:usersvc.userSch.CreateUser,
    db = Depends(get_db)
):
    result = usersvc.create_user(db, info)
    return Response(
        status=201,
        message="user created",
        data=result
    )
    

@user_router.patch("/{id}", response_model=Response[usersvc.userSch.User])
async def modify_user(
    id:int,
    info:usersvc.userSch.ModifyUser,
    db = Depends(get_db),
):
    result = usersvc.modify_user(db, id, info)
    return Response(
        status=200,
        message="user modified",
        data=result
    )
    pass

@user_router.delete("/{id}", response_model=Response[usersvc.userSch.User])
async def delete_user(
    id:int,
    db = Depends(get_db)
):
    result = usersvc.delete_user(db, id)
    return Response(
        status=200,
        message="user deleted",
        data=result
    )

@user_router.get("/{id}/groupe", response_model=Response[list[usersvc.groupeSch.Groupe]])
async def get_Groupe(
    id:int,
    db = Depends(get_db)
):
    result = usersvc.get_groupes_where_user(db, id)
    return Response(
        status=200,
        message="user groupes",
        data=result
    )