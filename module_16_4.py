from typing import Annotated, Dict
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=list[User])
async def get_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def add_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                 example="UrbanUser")], age: Annotated[int, Path(ge=18, le=120,
                                                                                                 description="Enter age",
                                                                                                 example="24")]) -> User:
    new_id = max((user.id for user in users), default=0) + 1
    #sers[new_id] = f"Имя: {username}, возраст: {age}"
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user
    #return f"User {new_id} is registered"


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: Annotated[int, Path(description="Enter user ID", example="1")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="Задача не найдена")


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: Annotated[int, Path(description="Enter user ID", example="1")]) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
