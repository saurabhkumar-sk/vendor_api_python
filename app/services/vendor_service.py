from app.repositories.vendor_repository import vendor_exists, create_vendor
from app.core.response import success_response, error_response,already_exixts_response
from app.core.security import create_access_token
from app.core.cloudnary_config import upload_image

# service for business logic

async def check_vendor_service(google_id: str,email:str):
    exists = await vendor_exists(google_id,email)
  
    if exists:
        return success_response(
            message="Vendor exists",
            data={"exists": True}
        )

    return error_response(
        message="Vendor not found",

        error_code="NOT_FOUND",
        data={"exists": False},
    )
    
    
# create vendor

async def create_vendor_service(request, shop_image, shop_logo):
    
    # 1. check if vendor already exists

    exists = await vendor_exists(request.google_id,request.email)
    
    if exists :
        return already_exixts_response( message="Vendor already exists",data= exists)
    
    shop_image_url = await upload_image(shop_image)
    
    shop_logo_url = None
    
    if shop_logo:
        shop_logo_url = await upload_image(shop_logo)
    
    
    
    # 2. prepare vendor data
    
    vendor_data = {
        "vendor_type" : "vendor",
        "google_id" : request.google_id,
        "shop_name" : request.shop_name,
        "vendor_name" : request.vendor_name,
        "shop_description" : request.shop_description,
        "phone_number" : request.phone_number,
        "phone_code" : request.phone_code,
        "email" : request.email,
        "website" : request.website,
        "address" : request.address,
        "latitude": request.latitude,   
        "longitude" : request.longitude,
        "shop_image" : shop_image_url,
        "shop_logo" : shop_logo_url,
        "business_licence_number" : request.business_licence_number,
        "tax_id_no" : request.tax_id_no,
        "establish_date" : request.establish_date,
        "number_of_employees" : request.number_of_employees,
        "facebook" : request.facebook,
        "instagram" : request.instagram,
        "twitter" : request.twitter,
        "youtube": request.youtube,  
        "delivery_type" : request.delivery_type,
        "delivery_fee" : request.delivery_fee,
        "free_delivery_amount" : request.free_delivery_amount,
        "avg_preparation_time" : request.avg_preparation_time,
        "is_pre_order" : request.is_pre_order             
    }
    
    # 3. insert into DB
    inserted_id = await create_vendor(vendor_data)
        
    # 4. create JWT token
    
    token = create_access_token({
        "vendor_id": str(inserted_id),
        "email": request.email
    })
    
    return success_response(message="Vendor create successfully",data={
        "token" : token,
        "vendor_id": str(inserted_id),
        "shop_image" : shop_image_url,
        "shop_logo_url" : shop_logo_url,
    })

    
    