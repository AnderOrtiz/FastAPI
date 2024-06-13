# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#Url local: http://127.0.0.1:8000

router= APIRouter(tags=["Users"])

#Iniciar el server: uvicorn users:app --reload

#Entidad user
class User(BaseModel):
    id: int
    name:str
    surname: str
    url: str
    age: int


userlist = [User(id=1, name= "Anderson", surname= "Ortiz", url= "https://ander.com", age= 18),
            User(id=2, name= "Brenner", surname= "Ortiz", url= "https://brenner.com", age= 22),
            User(id=3, name= "Lex", surname= "Ortiz", url= "https://lex.com", age= 27)
            ]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Anderson", "surname": "Ortiz", "url":"https://ander.com", "age": 18},
            {"name": "Brenner", "surname": "Ortiz", "url":"https://brenner.com", "age": 22},
            {"name": "Lex", "surname": "Ortiz", "url":"https://lex.com", "age": 27}]


#Path
@router.get("/user/{id}", response_model=User, status_code=200)
async def user(id:int):
    return search_user(id)


#Query
@router.get("/user/", response_model=User, status_code=200)
async def user(id:int):
    return search_user(id)


@router.get("/users/")
async def user():
    return userlist


@router.post("/user/",response_model=User ,status_code=201)
async def user(user:User):
    existing_user = search_user(user.id)
    if isinstance(existing_user, User):
        raise HTTPException(status_code=204, detail= f"El usuario {user.name} ya existe")
    else:
        userlist.append(user)
        index = userlist.index(user)
        return {"usuario creado exitosamente":userlist[index]}


@router.put("/user/", status_code=200)
async def user(user: User):
    found = False

    for index, saved_user in enumerate(userlist):
        if saved_user.id == user.id:
            userlist[index] = user
            found= True
            return user

    if not found:
        raise HTTPException(status_code=404, detail=f"El usuario {user.name} no se ha actualizado")


@router.delete("/user/{id}")
async def delete_user(id:int):
    found = False

    for index, saved_user in enumerate(userlist):
        if saved_user.id == id:
            del userlist[index]
            found = True
            return{"error": f"El usuario se ha eliminado"}

    if not found:
        return{"error": f"El usuario no se ha eliminado"}


def search_user(id):
    user = filter(lambda user:user.id == id, userlist)
    try:
        return list(user)[0]
    except:
        raise HTTPException(status_code=404, detail= "Usuario no encontrado")