from fastapi import HTTPException
from api.database import User, Session
import jwt
from werkzeug.security import check_password_hash
from api.config import Setting

ERROR_MSG = "number or password are invalid"

def login(number, password, db:Session) -> str:
    user = User.get(db, error_msg=ERROR_MSG, 
                    number=number)
    if check_password_hash(user.password, password):
        payload = {
            "id":user.id,
            "exp":None
        }
        jwt_token = jwt.encode(
            payload=payload,
            key=Setting.JWT_SECRET,
            # algorithm=Setting.JWT_ALGORITHM,
        )
        return jwt_token

    raise HTTPException(
        status_code=200,
        detail=ERROR_MSG,
    )
