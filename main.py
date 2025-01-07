from fastapi import FastAPI
import handlers
import handlers.feeds_handler
import handlers.news_handler

app = FastAPI()


@app.get("/news")
def read_news():
    return handlers.news_handler.read_news()


@app.get("feeds")
def read_feeds():
    return handlers.feeds_handler.get_feeds()