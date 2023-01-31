from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from utils import get_image_url


BASE_PATH = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))

router = APIRouter()


@router.get("/text-to-art/{task_id}", response_class=HTMLResponse)
async def generate_image_html(request: Request, task_id: str):
    img_url = await get_image_url(task_id)
    if img_url is None:
        raise HTTPException(status_code=404, detail="task_id is not found")
    return templates.TemplateResponse("index.html", {"request": request, "task_id": task_id, "img_url": img_url})
