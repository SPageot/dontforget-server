from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv  
from endpoints import api_router 
from slowapi import  _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware 
from slowapi.errors import RateLimitExceeded
from security.rate_limiter import limiter

load_dotenv()



app = FastAPI(title="Dont Forget Server", description="API for Dont Forget Client", version="1.0.0")
app.state.limiter = limiter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SlowAPIMiddleware)
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)

app.include_router(api_router)



