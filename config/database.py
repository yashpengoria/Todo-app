from pymongo import MongoClient

client = MongoClient("mongodb+srv://yashpengoria0505:BYNpp0360G@cluster0.2jehr46.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db=client.todo_db

collection_name=db["todo_collection"]