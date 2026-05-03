from fastapi import APIRouter, Depends, UploadFile, File
from app.schema.vendor_schema import CheckVendorRequest, CreateVendorRequest
from app.services.vendor_service import check_vendor_service,create_vendor_service
from app.schema.response_schema import SuccessResponse,ErrorResponse
import json
from typing import Union
from app.core.dependencies import get_vendor_profile
from app.services.vendor_service import get_profile_service
# endpoints


router = APIRouter()


@router.post('/check_vendor',response_model=Union[SuccessResponse, ErrorResponse])
async def check_vendor(payload : CheckVendorRequest ):
    return await check_vendor_service(payload.google_id,payload.email)


@router.post('/create_vendor')
async def create_vendor(
    payload: CreateVendorRequest = Depends(CreateVendorRequest.as_form),
    shop_image: UploadFile = File(None),
    shop_logo: UploadFile = File(None),
):
    return await create_vendor_service(
        payload,
        shop_image,
        shop_logo
    )
    
    
@router.get("/profile")
async def get_profile(vendor_id: str = Depends(get_vendor_profile)):
    return await get_profile_service(vendor_id)
