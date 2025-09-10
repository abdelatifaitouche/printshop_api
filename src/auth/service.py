
from sqlalchemy.orm.session import Session
from .models import User
from sqlalchemy import select
from .schemas import CreateUser , UserLogin
from fastapi.exceptions import HTTPException
from fastapi import status
from .utils.utils import generate_password_hash , validate_password , generate_token
from fastapi.responses import JSONResponse

class AuthService : 

    def get_user_by_email(self , user_email : str , db : Session) -> CreateUser:
        """
            get a user with the email provided 

        """

        user = db.execute(select(User).where(User.email == user_email)).scalars().first()

        if user is None : 
            raise Exception("No user found")

        

        return user
    

    def user_exists(self , user_email : str , db : Session)->bool :
        """ 

            check if the user exists using the email , generaly used in auth (login or signup)

        """

        user = db.execute(select(User).where(User.email == user_email)).first()

        if user is not None : 
            return True

        return False 

    def create_user(self , user_data : CreateUser , db :Session) -> CreateUser:

        """
            First we check if the email is already taken , if not create the user

        """

        user_email = user_data.email 

        if self.user_exists(user_email , db) : 
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="Email already taken")
        


        new_user = user_data.model_dump()

        password_hashed = generate_password_hash(user_data.password_hash)

        new_user["password_hash"] = password_hashed

        user = User(**new_user)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    


    def login_user(self , user_data :UserLogin , db : Session):

        user = self.get_user_by_email(user_data.email , db)

        if validate_password(user_data.password_hash , user.password_hash) : 
            
            user_payload = {
                    'email' : user.email , 'role' : user.role , 'username' : user.username 
                }

            access_token = generate_token(user_data=user_payload)
            refresh_token = generate_token(user_data=user_payload , refresh=True)

            return JSONResponse(
                content={
                    "access" : access_token , 
                    "refresh" : refresh_token,
                    "user" : user_payload
                } , status_code=status.HTTP_200_OK
            )
        
        



        return {'message' : "invalid creds"}
    
    
    
