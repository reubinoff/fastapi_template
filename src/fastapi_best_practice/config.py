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

    sql_uri = "sqlite:///foo.db"

    class Config:
        env_file = ".env"





configuration = Configuration()
