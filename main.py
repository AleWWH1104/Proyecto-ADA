import functions_framework
from dotenv import load_dotenv

from src.clients.maps_client import GoogleMapsClient
from src.config.settings import get_settings
from src.handlers.http_handler import handle_request
from src.services.places_service import PlacesService


# Carga el archivo .env en desarrollo local, en la nube no tiene efecto
load_dotenv()


# Construye el grafo de dependencias una sola vez por instancia
def _build_service() -> PlacesService:
    settings = get_settings()
    client = GoogleMapsClient(settings)
    return PlacesService(client)


_service = _build_service()


@functions_framework.http
def maps_query(request):
    body, status = handle_request(request, _service)
    return body, status
