from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def raiz():
    return {"Mensagem": "API da Escola no ar!"}