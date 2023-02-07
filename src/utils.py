import httpx
from loguru import logger
from pydantic import HttpUrl

from config import target_server_settings


async def get_image_url(task_id: str) -> HttpUrl:
    async with httpx.AsyncClient() as client:
        try:
            url = f"{target_server_settings.endpoint}/tasks/{task_id}/images"
            res = await client.get(url)
            data = res.json()
            grid_image_url = data["result"]["grid"]["url"]
        except Exception as e:
            logger.error(f"error: {e}")
            return None

    return grid_image_url


async def get_prompt(task_id: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            url = f"{target_server_settings.endpoint}/tasks/{task_id}/params"
            res = await client.get(url)
            data = res.json()
            prompt = data["params"]["prompt"]
        except Exception as e:
            logger.error(f"error: {e}")
            return None

    return prompt
