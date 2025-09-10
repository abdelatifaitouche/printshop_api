from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    JWT_SECRET : str
    JWT_ALGO : str

    class Config:
        env_file = "src.env"  # looks at project root

settings = Settings()
