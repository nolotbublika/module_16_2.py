from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_mane_page() -> dict:
    return {"message": " Главная страница"}


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": " Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_numbers(user_id: int) -> dict:
    return {"massage": f" Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def get_user_info(username:  str, age: int) -> dict:
    return {"User": username, "Age": age}


@app.get("/user/{username}/{age}")
async def enter_user_id(username: Annotated[str, Path(min_length=5, max_length=20
                                                       , description=" Введите ваш номер", exemple="бармалей")]
                        , age: Annotated[int, Path(ge=0, le=100, description="Введите свой возраст", exemple=45)]) -> dict:
    return {"User": username, "Age": age}
