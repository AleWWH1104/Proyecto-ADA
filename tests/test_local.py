from typing import Any

import pytest

from src.handlers.http_handler import handle_request
from src.services.places_service import PlacesService


# Cliente falso que evita llamadas reales al API durante las pruebas
class FakeMapsClient:
    def __init__(self, response: dict[str, Any]) -> None:
        self._response = response
        self.last_query: str | None = None

    def find_place(self, query: str, fields: str | None = None) -> dict[str, Any]:
        self.last_query = query
        return self._response


# Request falsa que imita la interfaz de Flask que usa Cloud Functions
class FakeRequest:
    def __init__(self, args: dict[str, str]) -> None:
        self.args = args


def test_servicio_retorna_datos_del_cliente():
    fake = FakeMapsClient({"status": "OK", "candidates": []})
    service = PlacesService(fake)
    result = service.search_by_text("Torre del Reformador")
    assert result["status"] == "OK"
    assert fake.last_query == "Torre del Reformador"


def test_servicio_rechaza_consulta_vacia():
    service = PlacesService(FakeMapsClient({}))
    with pytest.raises(ValueError):
        service.search_by_text("   ")


def test_handler_responde_400_sin_parametro_place():
    service = PlacesService(FakeMapsClient({}))
    body, status = handle_request(FakeRequest({}), service)
    assert status == 400
    assert "error" in body


def test_handler_responde_200_con_datos():
    fake = FakeMapsClient({"status": "OK", "candidates": [{"name": "X"}]})
    service = PlacesService(fake)
    body, status = handle_request(FakeRequest({"place": "Mercado Central"}), service)
    assert status == 200
    assert body["status"] == "OK"
