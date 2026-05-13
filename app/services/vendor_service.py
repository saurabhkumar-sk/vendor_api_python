from app.repositories.vendor_repository import vendor_exists, create_vendor, get_vendor_by_id, login_vendor
from app.core.response import success_response, error_response,already_exixts_response
from app.core.security import create_access_token
from app.core.cloudnary_config import upload_image
from app.models.vendor_models import vender_helper

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
    
    shop_image_url = None
    shop_logo_url = None
    
    if request.step != 0:
        if not shop_image:
             return error_response(
                message="Shop image is required",
                error_code="IMAGE_REQUIRED"
            )
             
        shop_image_url = await upload_image(shop_image)
    
    else :
        if shop_logo:
            shop_logo_url = await upload_image(shop_logo)
    
    if shop_logo:
        shop_logo_url = await upload_image(shop_logo)
    
    # 2. prepare vendor data
    
    vendor_data = {
        "step" : request.step,
        "type" : "vendor",
        "google_id" : request.google_id,
        "shop_name" : request.shop_name,
        "name" : request.name,
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



# vendor profile

async def get_profile_service(vendor_id:str):
    vendor = await get_vendor_by_id(vendor_id=vendor_id)
    # print("DB result:", vendor)
    
    if not vendor:
        return error_response(
            message="Vendor not found",
            error_code="NOT_FOUND",
        )
        
    vendor["id"] = str(vendor["_id"])
    del vendor["_id"]
    
    return success_response(
        message="Vendor profile fetched",
        data= vendor
    )
    
    
async def login_vendor_service(email : str, google_id : str):
    
    vendor = await login_vendor(email,google_id) # check vender exists or not in db
    
    if not vendor:
        return error_response(
            message= "Invalid credential",
            error_code= "INVALID_CREDENTIALS"
        )
        
    if vendor.get("step") != 3:
        return error_response(
            message="Complete profile setup first",
            error_code="PROFILE_INCOMPLETE",
            data={
                "current_step": vendor.get("step")
            }
        )

        
    token = create_access_token({
        "vendor_id" : str(vendor['_id']),
        "email" : vendor['email'],
    })
    
    
    return success_response(
        message="Login successful",
        data= {
            "token" : token,
            "vendor" : vender_helper(vendor)
         }
    )