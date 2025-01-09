from fastapi import FastAPI, HTTPException
from newsapi import NewsApiClient
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime
from typing import Optional
import os


load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
MONGO_DB_URI = os.getenv("MONGO_DB_URI")


client = MongoClient(MONGO_DB_URI)

db = client['DontForget']

collection = db['lists']

class UserList(BaseModel):
       passkey: str
       list: list[str]
       created: int = int(datetime.timestamp(datetime.now()))


def user_list_data(user):
       return {
              "list": user.list,
       }



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

class List(BaseModel):
      list: list[str]

class GetList(BaseModel):
      passkey:str

class UpdateList(BaseModel):
      passkey:str
      list:list[str]


@app.get("/news")
async def read_news():
            shopping_news: ResponseData = newsapi.get_everything(q="shopping", language='en', page=1, page_size=30)
            return {"data": shopping_news}

@app.post("/get-list")
async def read_list(passkey:GetList):
            list = collection.find_one({"passkey":passkey.passkey})
            return UserList(**list)

@app.put("/update-list")
async def read_list(update_list:UpdateList):
            collection.update_one({"passkey":update_list.passkey},{"$set":{"list":update_list.list}})
            updated_list = collection.find_one({"passkey":update_list.passkey})
            return updated_list


@app.post("/list")
async def add_to_list(item_list:UserList):
            try:
                  result = collection.insert_one(dict(item_list)) 
                  return {"status_code":200, "id":str(result.inserted_id)}
            except Exception as e:
                   return HTTPException(status_code=500, detail=f"Something went wrong: {e}")

