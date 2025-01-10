from endpoints import list, news

api_router = list.router

api_router.include_router(news.router)