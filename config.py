from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database configuration (individual fields)
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    # Or alternatively, as a single DATABASE_URL
    # database_url: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'




settings = Settings()