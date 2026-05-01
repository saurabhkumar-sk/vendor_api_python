def success_response(message: str, data=None):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(message: str, error_code: str,data=None):
    return {
        "success": False,
        "message": message,
        "error": error_code,
        "data": data
    }
    

def already_exixts_response(message : str,data=None):
    return {
        "success" : True,
        "message" : message,
        "data" : data
    }