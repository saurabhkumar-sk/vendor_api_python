from pydantic import BaseModel, Field,EmailStr
from typing import Annotated, Optional
from fastapi import Form

class CheckVendorRequest(BaseModel):
  email: EmailStr
  google_id: Annotated[
    str,
    Field(min_length=5, max_length=100, description="Google ID")
]
    
class CreateVendorRequest(BaseModel):
    google_id: Annotated[str, Field(..., description="Google UID")]
    
    # basic info
    email: EmailStr
    name: str
    type: str = "vendor"
    shop_name: Optional[str] = None
    shop_description: Optional[str] = None
    step: int = Form(0)

    # contact
    phone_number: Optional[str] = None
    phone_code: Optional[str] = None
    website: Optional[str] = None

    # location
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    # media
    shop_image: Optional[str] = None
    shop_logo: Optional[str] = None

    # legal
    business_licence_number: Optional[str] = None
    tax_id_no: Optional[str] = None
    establish_date: Optional[str] = None

    # business info
    number_of_employees: Optional[int] = None

    # social
    facebook: Optional[str] = None
    instagram: Optional[str] = None
    twitter: Optional[str] = None
    youtube: Optional[str] = None

    # delivery settings
    delivery_type: Optional[str] = None
    delivery_fee: Optional[float] = None
    free_delivery_amount: Optional[float] = None
    avg_preparation_time: Optional[int] = None
    is_pre_order: Optional[bool] = False
    
    @classmethod
    def as_form(
        cls,
        google_id: str = Form(...),
        email: EmailStr = Form(...),
        name: str = Form(...),
        shop_name: str = Form(None),
        type: str = Form("vendor"),
        shop_description: str = Form(None),
        step: int = Form(...), 
        
        phone_number: str = Form(None),
        phone_code: str = Form(None),
        website: str = Form(None),

        address: str = Form(None),
        latitude: float = Form(None),
        longitude: float = Form(None),

        business_licence_number: str = Form(None),
        tax_id_no: str = Form(None),
        establish_date: str = Form(None),

        number_of_employees: int = Form(None),

        facebook: str = Form(None),
        instagram: str = Form(None),
        twitter: str = Form(None),
        youtube: str = Form(None),

        delivery_type: str = Form(None),
        delivery_fee: float = Form(None),
        free_delivery_amount: float = Form(None),
        avg_preparation_time: int = Form(None),
        is_pre_order: bool = Form(False),
    ):
        return cls(
            google_id=google_id,
            step=step,
            email=email,
            name=name,
            type=type,
            shop_name=shop_name,
            shop_description=shop_description,
            phone_number=phone_number,
            phone_code=phone_code,
            website=website,
            address=address,
            latitude=latitude,
            longitude=longitude,
            business_licence_number=business_licence_number,
            tax_id_no=tax_id_no,
            establish_date=establish_date,
            number_of_employees=number_of_employees,
            facebook=facebook,
            instagram=instagram,
            twitter=twitter,
            youtube=youtube,
            delivery_type=delivery_type,
            delivery_fee=delivery_fee,
            free_delivery_amount=free_delivery_amount,
            avg_preparation_time=avg_preparation_time,
            is_pre_order=is_pre_order
        )