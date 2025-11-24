from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import Dict, Optional

# Инициализация приложения FastAPI
app = FastAPI(title="Mini API with Pydantic Validation")

# Pydantic-модель для валидации данных пользователя
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

    # Можно добавить валидацию полей (опционально)
    def __init__(self, **data):
        super().__init__(**data)

# Хранилище данных (в памяти, словарь)
users_db: Dict[int, User] = {
    1: User(id=1, name="John", email="john@example.com", age=20),
    2: User(id=2, name="Jane", email="jane@example.com", age=25),
    3: User(id=3, name="Bob", email="bob@example.com", age=30),
    4: User(id=4, name="Alice", email="alice@example.com", age=35),
    5: User(id=5, name="Tom", email="tom@example.com", age=40),
}

# Эндпоинт: получение списка всех пользователей
@app.get("/users", response_model=Dict[int, User])
def get_users():
    return users_db

# Эндпоинт: добавление нового пользователя
# @app.post("/users", response_model=User, status_code=201)
# def create_user(user: User):
#     if user.id in users_db:
#         raise HTTPException(status_code=400, detail="User with this ID already exists")
#     users_db[user.id] = user
#     return user

# Эндпоинт: получение пользователя по ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# Эндпоинт: обновление пользователя
# @app.put("/users/{user_id}", response_model=User)
# def update_user(user_id: int, user: User):
#     if user_id not in users_db:
#         raise HTTPException(status_code=404, detail="User not found")
#     users_db[user_id] = user
#     return user

# # Эндпоинт: удаление пользователя
# @app.delete("/users/{user_id}", status_code=204)
# def delete_user(user_id: int):
#     if user_id not in users_db:
#         raise HTTPException(status_code=404, detail="User not found")
#     del users_db[user_id]
#     return  # 204 No Content

# Запуск приложения
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)