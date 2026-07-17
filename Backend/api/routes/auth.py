from fastapi import APIRouter
from fastapi import HTTPException

from database.mongodb import (
    users_collection
)

from schemas.auth_schema import (
    SignupRequest,
    LoginRequest
)

from auth.auth_handler import (

    hash_password,

    verify_password,

    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# SIGNUP
@router.post("/signup")

async def signup(
    request: SignupRequest
):

    existing_user = await users_collection.find_one(

        {
            "email": request.email
        }
    )

    if existing_user:

        raise HTTPException(

            status_code=400,

            detail="Email already exists"
        )

    hashed_password = hash_password(
        request.password
    )

    user = {

        "name": request.name,

        "email": request.email,

        "password": hashed_password
    }

    result = await users_collection.insert_one(
        user
    )

    token = create_access_token(

        {
            "user_id":
            str(result.inserted_id)
        }
    )

    return {

        "token": token,

        "user": {

            "id":
            str(result.inserted_id),

            "name":
            request.name,

            "email":
            request.email
        }
    }


# LOGIN
@router.post("/login")

async def login(
    request: LoginRequest
):

    user = await users_collection.find_one(

        {
            "email": request.email
        }
    )

    if not user:

        raise HTTPException(

            status_code=400,

            detail="Invalid email or password"
        )

    valid_password = verify_password(

        request.password,

        user["password"]
    )

    if not valid_password:

        raise HTTPException(

            status_code=400,

            detail="Invalid email or password"
        )

    token = create_access_token(

        {
            "user_id":
            str(user["_id"])
        }
    )

    return {

        "token": token,

        "user": {

            "id":
            str(user["_id"]),

            "name":
            user["name"],

            "email":
            user["email"]
        }
    }