from fastapi import FastAPI

from routers import generate_html


def get_app() -> FastAPI:
    fast_api_app = FastAPI()
    fast_api_app.include_router(generate_html.router)
    return fast_api_app


app = get_app()
