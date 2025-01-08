from fastapi import FastAPI
from newsapi import NewsApiClient
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

app = FastAPI()

class Source(BaseModel):
      id: Optional[int] = None
      name: str

class Article(BaseModel):
      source: Source
      author: str
      title: str
      description:str
      url: str
      urlToImage: str
      publishedAt: str
      content: str

class News(BaseModel):
    status:str
    totalResults:int
    articles: list[Article]

class ResponseData(BaseModel):
      data:News


@app.get("/news")
async def read_news():
        shopping_news: ResponseData = newsapi.get_everything(q="shopping", language='en')
        return {"data": shopping_news}


@app.get("/feeds")
def read_feeds():
    return "hi"