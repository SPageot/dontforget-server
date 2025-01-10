from fastapi import APIRouter, HTTPException, Request
from model.model import UserList
from pymongo import collection, MongoClient
from security.rate_limiter import limiter
import os

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

client = MongoClient(MONGO_DB_URI)

db = client['DontForget']

collection = db['lists']

router = APIRouter()

@router.post("/get-list")
@limiter.limit("5/minute")
async def read_list(request:Request):
            passkey = await request.json()
            list = collection.find_one({"passkey":passkey["passkey"]})
            if list is None:
                    raise HTTPException(status_code=400, detail="No List Found!", headers={"X-Error": "Invalid Item ID"})
            return UserList(**list)


@router.put("/update-list")
@limiter.limit("5/minute")
async def update_list(request:Request):
            try:
                update_list = await request.json()
                collection.update_one({"passkey":update_list["passkey"]},{"$set":{"list":update_list["list"]}})
                updated_list = collection.find_one({"passkey":update_list["passkey"]})
                return UserList(**updated_list)
            except:
                raise HTTPException(status_code=500, detail="Something went wrong!")


@router.post("/list")
@limiter.limit("5/minute")
async def add_to_list(request:Request):
                try:
                    item_list = await request.json()
                    result = collection.insert_one(dict(item_list)) 
                    return {"status_code":200, "id":str(result.inserted_id)}
                except:
                    raise HTTPException(status_code=500, detail="Something went wrong!")            
            