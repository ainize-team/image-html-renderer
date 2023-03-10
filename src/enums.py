from enum import Enum


class StrEnum(str, Enum):
    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


class AppEnvEnum(StrEnum):
    DEV: str = "dev"
    PROD: str = "prod"
