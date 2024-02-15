from api.schemas import (
    groupe as groupeSch,
    user as userSch
)
from api.database import User, Groupe, UserInGroupe, Session, select
from fastapi import HTTPException

def create_groupe(
        db:Session,
        user_id:int,
        info:groupeSch.CreateGroupe,
) -> groupeSch.Groupe:
    if groupe:=Groupe.getOrNone(
        db, title=info.title, created_by=user_id
    ):
        raise HTTPException(
            status_code=400,
            detail=f"there is already a groupe name like {info.title}"
        )
    groupe = Groupe(
        title=info.title,
        description=info.description,
        created_by=user_id,
    )
    groupe.saveWithCommit(db)
    return groupeSch.Groupe.model_validate(groupe)

def modify_groupe(
        db:Session,
        user_id:int,
        groupe_id:int,
        info:groupeSch.ModifyGroupe,
)-> groupeSch.Groupe:
    if groupe:=Groupe.getOrNone(
        db, id=groupe_id, created_by=user_id
    ):
        if info.title:
            groupe.title = info.title
        if info.description:
            groupe.title = info.description
        groupe.saveWithCommit(db)
        return groupeSch.Groupe.model_validate(groupe)
    raise HTTPException(
        status_code=400,
        detail="can't modify the groupe"
    )

def delete_groupe(
        db:Session,
        user_id:int,
        groupe_id:int,
)-> groupeSch.Groupe:
    if groupe:=Groupe.getOrNone(
        db, id=groupe_id, created_by=user_id
    ):
        groupe.deleteWithCommit(db)
        return groupeSch.Groupe.model_validate(groupe)
    raise HTTPException(
        status_code=400,
        detail="can't delete the groupe"
    )

def get_users_in_groupe(
        db:Session,
        groupe_id:int,
) -> list[userSch.User]:
    query = select(User).join(
        UserInGroupe,
        User.id == UserInGroupe.user_id
    ).filter(
        UserInGroupe.groupe_id == groupe_id
    )

    result = db.scalars(query).all()
    result = [userSch.User.model_validate(x) for x in result]

    return result
