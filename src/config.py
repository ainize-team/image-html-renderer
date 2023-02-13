from pydantic import BaseSettings

from enums import AppEnvEnum


class TargetServerSettings(BaseSettings):
    endpoint: str = ""
    app_env: AppEnvEnum = AppEnvEnum.PROD


target_server_settings = TargetServerSettings()
