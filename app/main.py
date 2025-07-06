from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_root():
    return {"mensaje": "soy rafael tapia morales"}