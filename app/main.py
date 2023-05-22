from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache

from .nytime_client import get_top_stories
from .story_formatter import format_stories_to_string
from .summarizer import summarise_news_stories

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000" "http://localhost:8080",
    "http://127.0.0.1:5500/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
@cache(namespace="test", expire=6000)
def index():
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
    FastAPICache.init(InMemoryBackend())
