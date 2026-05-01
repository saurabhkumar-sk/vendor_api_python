from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "my_secret_key"   
ALGORITHM = "HS256"

def create_access_token(data : dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(days=7) 
    
    to_encode.update({'exp' : expire})
    
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return token

