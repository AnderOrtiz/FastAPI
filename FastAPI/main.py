# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI 

#Url local: http://127.0.0.1:8000

app= FastAPI()

@app.get("/")
async def root():
    return({"message":"Hello word"})

#Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def userjson():
    return {"url":"https://mouredev.com/python"}

#Iniciar el server: uvicorn main:app --reload

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
