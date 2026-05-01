def vender_helper(vendor) -> dict:
    return {
        "id" : str(vendor["_id"]),
        "name" : vendor["name"],
        "email" : vendor['email'],
        "google_id" : vendor['google_id']
    }