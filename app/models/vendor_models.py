# def vender_helper(vendor) -> dict:
#     return {
#         "id" : str(vendor["_id"]),
#         "name" : vendor["name"],
#         "email" : vendor['email'],
#         # "google_id" : vendor['google_id']
#     }

def vender_helper(vendor) -> dict:
    return {
        "id": str(vendor["_id"]),
        "step": vendor.get("step"),
        "type": vendor.get("type"),
        "google_id": vendor.get("google_id"),

        "shop_name": vendor.get("shop_name"),
        "name": vendor.get("name"),
        "shop_description": vendor.get("shop_description"),

        "phone_number": vendor.get("phone_number"),
        "phone_code": vendor.get("phone_code"),
        "email": vendor.get("email"),
        "website": vendor.get("website"),

        "address": vendor.get("address"),
        "latitude": vendor.get("latitude"),
        "longitude": vendor.get("longitude"),

        "shop_image": vendor.get("shop_image"),
        "shop_logo": vendor.get("shop_logo"),

        "business_licence_number": vendor.get("business_licence_number"),
        "tax_id_no": vendor.get("tax_id_no"),
        "establish_date": vendor.get("establish_date"),

        "number_of_employees": vendor.get("number_of_employees"),

        "facebook": vendor.get("facebook"),
        "instagram": vendor.get("instagram"),
        "twitter": vendor.get("twitter"),
        "youtube": vendor.get("youtube"),

        "delivery_type": vendor.get("delivery_type"),
        "delivery_fee": vendor.get("delivery_fee"),
        "free_delivery_amount": vendor.get("free_delivery_amount"),
        "avg_preparation_time": vendor.get("avg_preparation_time"),

        "is_pre_order": vendor.get("is_pre_order"),
    }