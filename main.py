from fastapi import FastAPI
from config.config import get_repo_adapter
from adapters.http.controllers import setup_routes

repo = get_repo_adapter()
app = FastAPI()
app.include_router(setup_routes(repo))
