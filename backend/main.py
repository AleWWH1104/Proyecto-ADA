"""Entry point de la Cloud Function. Recibe el request HTTP y delega al handler."""
import functions_framework

from src.handler import handle_request


@functions_framework.http
def optimize_route(request):
    return handle_request(request)
