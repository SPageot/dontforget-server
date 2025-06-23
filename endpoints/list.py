from fastapi import APIRouter, HTTPException, Request
from model.model import UserList
from pymongo.mongo_client import MongoClient
from security.rate_limiter import limiter
import os

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

client = MongoClient(MONGO_DB_URI)

db = client['DontForget']

collection = db['lists']

router = APIRouter()

async def checkIfPasskeyExists(passkey):
        list = collection.find_one({"passkey":passkey})
        if list is None:
                return False
        else:
                return True

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
                    doesPassKeyExist = await checkIfPasskeyExists(item_list['passkey'])
                    if doesPassKeyExist is not True:
                        result = collection.insert_one(item_list) 
                        return {"status_code":200, "id":str(result.inserted_id)}
                    else:
                        raise HTTPException(status_code=400, detail="Passkey already taken")
                except Exception as e:
                    print(e)
                    raise HTTPException(status_code=500, detail=f"Error: {e}")            
            