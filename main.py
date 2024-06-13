# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI 
from routers import products, users, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

#Url local: http://127.0.0.1:8000

app= FastAPI()

#router
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Home"])
async def root():
    return({"message":"Hello word"})

#Url local: http://127.0.0.1:8000/url

@app.get("/url", tags=["Home"])
async def userjson():
    return {"url":"https://mouredev.com/python"}

#Iniciar el server: uvicorn main:app --reload

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
