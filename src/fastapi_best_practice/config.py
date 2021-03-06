import os 

from pydantic import BaseSettings, BaseModel, Field


class SettingOfSomeModel(BaseModel):
    foo: str = Field(default="asasd", env='my_foo_value')
    apple = 1


class Configuration(BaseSettings):
    log_level: str = "DEBUG"
    env: str = "local"

    sentry_dsn: str = ""
    app_name: str = "Awesome Project"
    admin_email: str
    some_model: SettingOfSomeModel = SettingOfSomeModel()

    db_name = "fastapi_best_practice_core"
    db_pass = "sql"
    db_host = "localhost"
    

    
    alembix_ini = f"{os.path.dirname(os.path.realpath(__file__))}/alembic.ini",

    class Config:
        env_file = ".env"



configuration = Configuration()
