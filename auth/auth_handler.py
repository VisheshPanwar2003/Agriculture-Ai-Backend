from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from passlib.context import (
    CryptContext
)

SECRET_KEY = "agrisense_secret"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 7 * 24 * 60

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# HASH PASSWORD
def hash_password(
    password
):

    # BCRYPT MAX LIMIT FIX
    password = password[:72]

    return pwd_context.hash(
        password
    )


# VERIFY PASSWORD
def verify_password(
    plain_password,
    hashed_password
):

    # BCRYPT MAX LIMIT FIX
    plain_password = plain_password[:72]

    return pwd_context.verify(

        plain_password,

        hashed_password
    )


# CREATE JWT TOKEN
def create_access_token(
    data: dict
):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(

        minutes=
        ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM
    )


# VERIFY TOKEN
def verify_token(
    token: str
):

    try:

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None