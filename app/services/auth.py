from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY = "123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

clients = {"test_client_id": "test_client_secret"}


class Token(BaseModel):
    access_token: str
    token_type: str


async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        exp = payload.get("exp")
        if exp is None or datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(
            timezone.utc
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@auth_router.post("/token", response_model=Token, tags=["Auth Service"])
async def token(client_id: str = Form(...), client_secret: str = Form(...)):
    if clients.get(client_id) != client_secret:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid client credentials",
        )

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {"sub": client_id, "exp": expire.timestamp()}

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
