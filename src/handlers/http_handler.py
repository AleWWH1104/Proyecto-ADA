from typing import Any

import requests

from src.services.places_service import PlacesService


# Procesa la request HTTP y delega al servicio de lugares
def handle_request(request: Any, service: PlacesService) -> tuple[dict[str, Any], int]:
    place = request.args.get("place", "") if hasattr(request, "args") else ""
    fields = request.args.get("fields") if hasattr(request, "args") else None

    if not place:
        return {"error": "parametro 'place' requerido"}, 400

    try:
        data = service.search_by_text(place, fields)
        return data, 200
    except ValueError as exc:
        return {"error": str(exc)}, 400
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else 502
        return {"error": "fallo al consultar la API de Maps", "detail": str(exc)}, status
    except requests.RequestException as exc:
        return {"error": "error de red al consultar la API", "detail": str(exc)}, 502
