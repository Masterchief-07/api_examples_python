from api.schemas import (
    user as userSch,
    groupe as groupeSch,
)
from api.database import User, Session, UserInGroupe, select, Groupe
from werkzeug.security import generate_password_hash
from fastapi import HTTPException

def create_user(
        db:Session,
        info:userSch.CreateUser,
) -> userSch.User:

    if User.getOrNone(db, 
        numero = info.numero):
        raise HTTPException(
            status_code=400,
            detail="number actully used in a request",
        )

    user = User(
        nom=info.nom,
        number=info.numero,
        password=generate_password_hash(info.password)
    )
    user.saveWithCommit(db)
    result = userSch.User.model_validate(user)
    return result

def modify_user(
        db:Session,
        user_id:int,
        info: userSch.CreateUser,
) -> userSch.User:
    if user:=User.getOrNone(
        db,
        id=user_id,
    ): 
        if info.nom:
            user.nom = info.nom
        if info.numero:
            user.number = info.numero
        if info.password:
            user.password = info.password
        user.saveWithCommit(db)
        return userSch.User.model_validate(user)
    else:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )

def delete_user(
        db:Session,
        user_id:int,
) -> userSch.User:
    if user:=User.getOrNone(
        db,
        id=user_id,
    ): 
        user.deleteWithCommit(db)
        return userSch.User.model_validate(user)
    else:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )

def get_groupes_where_user(
        db:Session,
        user_id:int,
) -> list[groupeSch.Groupe]:
    query = select(Groupe).join(
        UserInGroupe,
        Groupe.id == UserInGroupe.groupe_id
    ).filter(
        UserInGroupe.user_id == user_id
    )

    result = db.scalars(query).all()
    result = [groupeSch.Groupe.model_validate(x) for x in result]

    return result
    pass
