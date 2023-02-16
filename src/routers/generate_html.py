from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config import target_server_settings
from enums import AppEnvEnum
from utils import get_image_url, get_prompt


BASE_PATH = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))

router = APIRouter()


@router.get("/{task_id}", response_class=HTMLResponse)
async def generate_image_html(request: Request, task_id: str):
    img_url = await get_image_url(task_id)
    prompt = await get_prompt(task_id)
    if img_url is None:
        raise HTTPException(status_code=404, detail="task_id is not found")

    og_url = f"https://aindao-text-to-art.ainetwork.xyz/{task_id}"
    if target_server_settings.app_env == AppEnvEnum.DEV:
        og_url = f"https://aindao-text-to-art-dev.ainetwork.xyz/{task_id}"

    return templates.TemplateResponse(
        "index.html", {"request": request, "task_id": task_id, "img_url": img_url, "og_url": og_url, "prompt": prompt}
    )
