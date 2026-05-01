import os
from dataclasses import dataclass
from functools import lru_cache


# Configuracion inmutable cargada desde variables de entorno
@dataclass(frozen=True)
class Settings:
    api_key: str
    api_url: str
    default_fields: str
    timeout_seconds: int


# Valida que la variable exista y no este vacia
def _require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Variable de entorno requerida no definida: {name}")
    return value


# Lee una variable opcional con valor por defecto
def _optional_env(name: str, default: str) -> str:
    value = os.environ.get(name, "").strip()
    return value if value else default


# Cachea la configuracion para evitar releer el entorno en cada request
@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings(
        api_key=_require_env("MAPS_KEY"),
        api_url=_optional_env(
            "MAPS_API_URL",
            "https://maps.googleapis.com/maps/api/place/findplacefromtext/json",
        ),
        default_fields=_optional_env(
            "MAPS_DEFAULT_FIELDS",
            "place_id,name,geometry,formatted_address",
        ),
        timeout_seconds=int(_optional_env("MAPS_TIMEOUT_SECONDS", "10")),
    )
