from fastapi import APIRouter

from app.api.endpoints import items, list  # ,login, users

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(list.router, prefix="/list", tags=["list"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
