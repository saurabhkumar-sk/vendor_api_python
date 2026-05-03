from app.core.database import db
from bson import ObjectId

# // database code

async def vendor_exists(google_id: str,email:str) -> bool:
    vendor = await db.vendors.find_one(
        {
          "$or" : [
           {"google_id": google_id},
           {"email" : email}   
          ]
        },
        {"_id": 1}
    )
    return vendor is not None


async def create_vendor(vendor_data: dict):
    result = await db.vendors.insert_one(vendor_data)
    print(result.inserted_id)
    return result.inserted_id
async def get_vendor_by_id(vendor_id: str):
    try:
        vendor = await db.vendors.find_one({
            "_id": ObjectId(vendor_id)
        })
        return vendor
    except Exception as e:
        print("ObjectId Error:", e)
        return None