from fastapi import APIRouter
ON_STARTUP = []
ON_SHUTDOWN = []
api_router = APIRouter(prefix="/api/v2", on_startup=ON_STARTUP, on_shutdown=ON_SHUTDOWN)
