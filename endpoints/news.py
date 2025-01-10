from fastapi import APIRouter, HTTPException, Request
from model.model import ResponseData
from newsapi import NewsApiClient
from security.rate_limiter import limiter
import os



NEWS_API_KEY = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

router = APIRouter()

@router.get("/news")
@limiter.limit("5/minute")
async def get_news_feed(request:Request):
            shopping_news: ResponseData = newsapi.get_everything(q="shopping", language='en', page=1, page_size=30)
            return {"data": shopping_news}

