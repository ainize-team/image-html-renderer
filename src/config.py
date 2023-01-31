from pydantic import BaseSettings


class TargetServerSettings(BaseSettings):
    endpoint: str = ""


target_server_settings = TargetServerSettings()
