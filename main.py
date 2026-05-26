from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ROUTES
from api.routes.analysis import (
    router as analysis_router
)

from api.routes.chatbot import (
    router as chatbot_router
)

from api.routes.weather import (
    router as weather_router
)

from api.routes.almanac import (
    router as almanac_router
)

from api.routes.vision import (
    router as vision_router
)

from api.routes.auth import (
    router as auth_router
)

# FASTAPI APP
app = FastAPI(

    title="AgriSense AI Backend",

    version="1.0.0"
)

# CORS
app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# ROUTES
app.include_router(
    analysis_router
)

app.include_router(
    chatbot_router
)

app.include_router(
    weather_router
)

app.include_router(
    almanac_router
)

app.include_router(
    vision_router
)

app.include_router(
    auth_router
)

# HOME ROUTE
@app.get("/")

async def home():

    return {

        "message":
        "AgriSense AI Backend Running"
    }