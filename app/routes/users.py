from fastapi import APIRouter
from app.database import users_collection
from app.models import user_serializer
from bson import ObjectId

router = APIRouter()

@router.post("/users")
def create_user(user: dict):
    result = users_collection.insert_one(user)
    return {"id": str(result.inserted_id)}

@router.get("/users")
def get_users():
    users = users_collection.find()
    return [user_serializer(user) for user in users]

@router.get("/users/{id}")
def get_user(id: str):
    user = users_collection.find_one({"_id": ObjectId(id)})
    return user_serializer(user)

@router.put("/users/{id}")
def update_user(id: str, user: dict):
    users_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": user}
    )
    return {"message": "Usuario actualizado"}

@router.delete("/users/{id}")
def delete_user(id: str):
    users_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Usuario eliminado"}