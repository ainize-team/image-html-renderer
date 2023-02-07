from pydantic import BaseSettings


class TargetServerSettings(BaseSettings):
    endpoint: str = ""
    branch: str = ""


target_server_settings = TargetServerSettings()
