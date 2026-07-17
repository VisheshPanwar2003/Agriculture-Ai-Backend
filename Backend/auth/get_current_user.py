from fastapi import Header
from fastapi import HTTPException

from auth.auth_handler import (
    verify_token
)


async def get_current_user(
    authorization: str = Header(None)
):

    if not authorization:

        raise HTTPException(

            status_code=401,

            detail="Unauthorized"
        )

    try:

        token = authorization.split(
            " "
        )[1]

        payload = verify_token(
            token
        )

        return payload

    except:

        raise HTTPException(

            status_code=401,

            detail="Invalid token"
        )