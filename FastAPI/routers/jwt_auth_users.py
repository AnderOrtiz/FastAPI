from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta  


ALGORITH = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"


router = APIRouter(tags=["jwt_auth_users"])


oauth2 = OAuth2PasswordBearer(tokenUrl="login")


crypt = CryptContext(schemes=["bcrypt"])


# Entidad user
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disable: bool


class UserDB(User):
    password: str


users_db = {
    "Ander": {
        "username": "Ander",
        "fullname": "Anderson Ortiz",
        "email": "ander@ej.com",
        "disable": False,
        "password": "$2a$12$0Z4RXeplsnqVQs7pNQHUAezfCfyWKtJ/TO9nzFNCpRVVSmah30UlO"
    },
    "Ana": {
        "username": "Ana",
        "fullname": "Ana Gómez",
        "email": "ana@ej.com",
        "disable": False,
        "password": "$2a$12$ZJsGz3./fomBAlmkx5LH0.10ntYDFQGHaQyq3F37Z44law2VBkvLy"
    },
    "Juan": {
        "username": "Juan",
        "fullname": "Juan Pérez",
        "email": "juan@ej.com",
        "disable": True,
        "password": "$2a$12$bo4h3SPOAS0iLiRgILeqX.f0yINpkRtmWuMAaU8dWqdNP.mbnuxZ2"
    },
    "Maria": {
        "username": "Maria",
        "fullname": "Maria Rodríguez",
        "email": "maria@ej.com",
        "disable": False,
        "password": "123456" #"mypass"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token:str = Depends(oauth2)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales no validas",
                            headers={"WWW-Authenticate": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITH]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disable:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User inactivo"
        )

    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )

    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITH), "toekn_type":"bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user