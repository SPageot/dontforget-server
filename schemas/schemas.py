from pydantic import BaseModel

class List(BaseModel):
      list: list[str]

class GetList(BaseModel):
      passkey: str

class UpdateList(BaseModel):
      passkey: str
      list: list[str]