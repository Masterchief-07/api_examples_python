from fastapi import APIRouter, Depends, HTTPException
from api.services import (
    groupe as groupesvc
)
from api.database import get_db
from api.schemas.response import Response

groupe_router = APIRouter()

@groupe_router.get("/")
async def get_groupe():
    pass

@groupe_router.post("/", response_model=Response[groupesvc.groupeSch.Groupe])
async def create_groupe(
    user_id:int,
    info:groupesvc.groupeSch.CreateGroupe,
    db = Depends(get_db)
):
    result = groupesvc.create_groupe(db, user_id, info)
    return Response(
        status=201,
        message = "groupe created",
        data=result
    )
    

@groupe_router.patch("/{groupe_id}", response_model=Response[groupesvc.groupeSch.Groupe])
async def modify_groupe(
    groupe_id:int,
    user_id:int,
    info:groupesvc.groupeSch.ModifyGroupe,
    db = Depends(get_db),
):
    result = groupesvc.modify_groupe(db, user_id,groupe_id, info)
    return Response(
        status=200,
        message = "groupe modified",
        data=result
    )
    pass

@groupe_router.delete("/{groupe_id}", response_model=Response[groupesvc.groupeSch.Groupe])
async def delete_groupe(
    groupe_id:int,
    user_id:int,
    db = Depends(get_db)
):
    result = groupesvc.delete_groupe(db, user_id, groupe_id)
    return Response(
        status=200,
        message = "groupe deleted",
        data=result
    )

@groupe_router.get("/{id}/users", response_model=Response[list[groupesvc.userSch.User]])
async def get_users(
    id:int,
    db = Depends(get_db)
):
    result = groupesvc.get_users_in_groupe(db, id)
    return Response(
        status=200,
        message = "groupe users",
        data=result
    )