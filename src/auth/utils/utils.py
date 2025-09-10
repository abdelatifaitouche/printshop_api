from passlib.context import CryptContext
from datetime import timedelta , datetime
import jwt

hash_context = CryptContext(schemes=['bcrypt'])



def generate_password_hash(password_str : str) -> str:
    """
        Creates a password hash using the passlib Crypt Context
        with the bcrypt algo  (we might change this to argon2 but f it)

    """
    password_hash = hash_context.hash(password_str)

    return password_hash



def validate_password(password : str , password_hash : str) -> bool:
    """
        Inputs : Loggin password , password_hash saved in the db

        returns True : if the passwords matches or False otherwise
    """
    return hash_context.verify(password , password_hash)




def generate_token(user_data : dict , expiry_time : timedelta = None , refresh : bool = False) -> str:

    payload = {}

    payload["user"] = user_data
    payload["exp"] = datetime.now() + (expiry_time if expiry_time is not None else timedelta(hours=10))
    payload["refresh"] = refresh

    SECRET_KEY = "4e8a6e06b657649066383de4d2d2cd18741dbe23"

    token : str = jwt.encode(payload=payload , key=SECRET_KEY , algorithm="HS256")

    return token




def decode_token(token : str) -> dict:
    try : 
        decoded = jwt.decode(token , key="4e8a6e06b657649066383de4d2d2cd18741dbe23" , algorithms=["HS256"])
        if decoded["exp"] > datetime.now() : 
            return decoded
    except jwt.PyJWTError as e :
        return {}