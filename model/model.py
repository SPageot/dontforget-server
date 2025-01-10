from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserList(BaseModel):
       passkey: str
       list: list[str]
       created: int = int(datetime.timestamp(datetime.now()))


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
    status: str
    totalResults: int
    articles: list[Article]

class ResponseData(BaseModel):
      data: News