from pydantic import BaseModel



class CommandBase(BaseModel):
    title : str

    class Config : 
        orm_mode : True


class CreateCommand(CommandBase):
    class Config : 
        orm_mode : True 