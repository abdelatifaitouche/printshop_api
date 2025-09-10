from typing import Coroutine
from typing_extensions import Annotated, Doc
from fastapi import Request
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from .utils.utils import decode_token


class JwtBearer(HTTPBearer):
    
    def __init__(self,auto_error: bool = True):
        super().__init__(auto_error=auto_error)


    async def __call__(self, request: Request):
        data = await super().__call__(request)
        token = data.credentials


        if not self.verify_token(token) : 
            raise Exception("an error has occured")

        token_data = decode_token(token)


        return token_data

    def verify_token(self , token : str)->bool : 
        try : 
            decoded_token = decode_token(token)
        except : 
            print("an error has occured")

        if decoded_token :
            return True
        return False 
