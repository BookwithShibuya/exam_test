from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock database
fake_users_db = {
    "user1": "password1",
    "user2": "password2",
}

# Mock reward data
items = [
    {"id": 1, "name": "Reward Item A", "points": 100, "expiry": "2024-01-01"},
    {"id": 2, "name": "Reward Item B", "points": 200, "expiry": "2025-01-01"},
    {"id": 3, "name": "Reward Item C", "points": 300, "expiry": "2024-06-01"}
]

# Request model for login
class LoginRequest(BaseModel):
    username: str
    password: str


# Login route
@app.post("/login")
async def login(data: LoginRequest):
    if data.username in fake_users_db and fake_users_db[data.username] == data.password:
        return {"token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid username or password")


# Rewards API
@app.get("/rewards")
async def get_rewards():
    return {"rewards": items}
