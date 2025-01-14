from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def welcome_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def userinfo(username: str, userage: int) -> dict:
    return {"Информация о пользователе. Имя": username, "Возраст": userage}
