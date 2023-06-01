import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from .nytimes_client import get_top_stories
from .story_formatter import format_stories_to_string
from .summariser import summarise_news_stories

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5500/",  # Live server default
    "https://summer-ui.fly.dev/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"msg": "Welcome to the News App"}


@app.get("/news")
@cache(namespace="test", expire=21600)
def news():
    summary = ""
    images = []
    try:
        stories = get_top_stories()
        for story in stories:
            images.extend(story["multimedia"])
        summary = summarise_news_stories(format_stories_to_string(stories))
        print(summary)
        images = list(
            filter(lambda image: image["format"] == "Large Thumbnail", images)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="Apologies, something bad happened :("
        )
    return {"summary": summary, "images": images}


@app.on_event("startup")
async def startup():
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")
    redis = aioredis.from_url(REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
