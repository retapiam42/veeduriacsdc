from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_root():
    return {"mensaje": "Hola mundo"}