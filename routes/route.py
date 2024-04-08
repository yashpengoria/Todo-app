from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router=APIRouter()

#GET request method

@router.get("/")
async def get_todos():
    todos=list_serial(collection_name.find())
    return todos

#POST request method

@router.post("/")
async def post_todos(todo:Todo):
    collection_name.insert_one(dict(todo))

#PUT request method

@router.put("/{id}")
async def put_todos(id: str, todo:Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})

#Delete request method

@router.delete("/{id}")
async def delete_todos(id:str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})