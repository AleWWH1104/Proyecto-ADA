from typing import Any

from src.clients.maps_client import MapsClient


# Servicio que coordina la busqueda de lugares contra el cliente de Maps
class PlacesService:
    def __init__(self, client: MapsClient) -> None:
        self._client = client

    # Recibe un texto y devuelve los datos geograficos del lugar
    def search_by_text(self, query: str, fields: str | None = None) -> dict[str, Any]:
        cleaned = query.strip()
        if not cleaned:
            raise ValueError("La consulta no puede estar vacia")
        return self._client.find_place(cleaned, fields)
