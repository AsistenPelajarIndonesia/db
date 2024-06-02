from pydantic import BaseModel
from database_operations import user_operation
from db.api_router import api_router

class User(BaseModel):
    name: str
    email: str
    password: str
    information: str

class UpdateUserModel(BaseModel):
    name: str
    property_name: str
    property_value: str

@api_router.get("/users/get/{name}")
def get_user(name: str):
    user = user_operation.select_user(name)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "information": user.information
    }

@api_router.get("/users/exists/{name}")
def user_exists(name: str):
    return {
        "response": user_operation.user_exists(name)
    }

@api_router.post("/users/create")
def create_user(user: User):
    user_operation.create_user(
        name=user.name,
        email=user.email,
        password=user.password,
        information=user.information
    )
    user = user_operation.select_user(user.name)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "information": user.information
    }

@api_router.post("/users/update")
def update_user(user: UpdateUserModel):
    user_operation.update_user(
        name=user.name, 
        property_name=user.property_name, 
        property_value=user.property_value
    )
    user = user_operation.select_user(user.name)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "information": user.information
    }

@api_router.get("/users/delete/{name}")
def delete_user(name: str):
    user_operation.delete_user(name)
    return {
        "response": "DELETED"
    }


