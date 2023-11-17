from fastapi import FastAPI

from app.api.api import api_router
from app.models.init_db import init_db

app = FastAPI(title="FluDo")
init_db(app)

app.include_router(api_router)
