from fastapi import APIRouter

from services.almanac_service import (
    FarmersAlmanac
)

router = APIRouter(
    prefix="/almanac",
    tags=["Almanac"]
)

almanac = FarmersAlmanac()

@router.get("/daily")

async def daily_almanac():

    return almanac.get_daily_almanac()


@router.get("/seasonal/{region}")

async def seasonal_guide(
    region: str
):

    return almanac.get_seasonal_guide(
        region
    )


@router.get("/crop-ai/{crop_name}")

async def crop_ai_data(
    crop_name: str
):

    return almanac.get_crop_ai_data(
        crop_name
    )