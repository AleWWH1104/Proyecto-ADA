# Laboratorio Google Maps API - Cloud Function

Cloud Function en Python que consulta la API de Google Maps Places.

## Estructura

```
maps-lab/
├── pyproject.toml          # Dependencias gestionadas con uv
├── .env.example            # Plantilla de variables de entorno
├── .gitignore              # Excluye secretos y artefactos
├── main.py                 # Punto de entrada de la Cloud Function
├── src/
│   ├── config/
│   │   └── settings.py     # Carga y valida configuracion
│   ├── clients/
│   │   └── maps_client.py  # Cliente HTTP de Google Maps
│   ├── services/
│   │   └── places_service.py  # Logica de negocio
│   └── handlers/
│       └── http_handler.py # Procesa la request HTTP
├── tests/
│   └── test_local.py       # Pruebas locales
└── notebooks/
    └── prototype.ipynb     # Prototipo en Jupyter
```

## Pasos rapidos

1. `uv sync` para instalar dependencias
2. Copiar `.env.example` a `.env` y poner tu `MAPS_KEY`
3. `uv run functions-framework --target=maps_query --port=8080`
4. `curl "http://localhost:8080?place=Torre+del+Reformador+Guatemala"`
