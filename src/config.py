from pydantic import BaseSettings


class TargetServerSettings(BaseSettings):
    endpoint: str = ""
    app_env: str = "prod"


target_server_settings = TargetServerSettings()
