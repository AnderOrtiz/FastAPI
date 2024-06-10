# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI 
from pydantic import BaseModel

#Url local: http://127.0.0.1:8000

app= FastAPI()

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

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Anderson", "surname": "Ortiz", "url":"https://ander.com", "age": 18},
            {"name": "Brenner", "surname": "Ortiz", "url":"https://brenner.com", "age": 22},
            {"name": "Lex", "surname": "Ortiz", "url":"https://lex.com", "age": 27}]


@app.get("/users")
async def users():
    return userlist