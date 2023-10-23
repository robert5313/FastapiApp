from fastapi import APIRouter
from models.users import User
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

#Get Request Method
@router.get("/")
async def get_users():
    users = list_serial(collection_name.find())
    return users

# Post Request Method
@router.post("/")
async def post_user(user: User):
    collection_name.insert_one(dict(user))


# Put Request Method
@router.put("/{id}")
async def put_user(id: str, user: User):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})


# Delete Request Method
@router.delete("/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})