from fastapi import Depends, HTTPException, status
from app.config.config import settings
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt,JWTError

security = HTTPBearer()


def get_vendor_profile(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    print(token)
    
    try:
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        vendor_id : str = payload.get("vendor_id") 
        
        if vendor_id is None:
            raise HTTPException(
                status_code= status.HTTP_401_UNAUTHORIZED,
                detail= "Invalid Token"
            )
            
        return vendor_id
    
    except JWTError:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid or expired"
        )    
            