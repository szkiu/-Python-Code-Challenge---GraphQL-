from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

SECRET_KEY = "your_secret_key"

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

clients = {"client_id": "client_secret"}


@auth_router.post("/token")
async def token(client_id: str, client_secret: str):
    if clients.get(client_id) != client_secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid client credentials",
        )

    token_data = {"sub": client_id}
    token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}
