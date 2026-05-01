from typing import Any, Protocol

import requests

from src.config.settings import Settings


# Contrato del cliente para permitir reemplazos en pruebas o nuevas implementaciones
class MapsClient(Protocol):
    def find_place(self, query: str, fields: str | None = None) -> dict[str, Any]: ...


# Implementacion concreta que llama a la API de Google Maps
class GoogleMapsClient:
    def __init__(self, settings: Settings, http_session: requests.Session | None = None) -> None:
        self._settings = settings
        self._session = http_session or requests.Session()

    # Busca un lugar por texto libre y retorna la respuesta cruda del API
    def find_place(self, query: str, fields: str | None = None) -> dict[str, Any]:
        params = {
            "input": query,
            "inputtype": "textquery",
            "fields": fields or self._settings.default_fields,
            "key": self._settings.api_key,
        }
        response = self._session.get(
            self._settings.api_url,
            params=params,
            timeout=self._settings.timeout_seconds,
        )
        response.raise_for_status()
        return response.json()
