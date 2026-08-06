from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def raiz():
    return {"Mensagem": "API da Escola no ar!"}

@app.get ("/status")
def status():
    return{"Status":"OK", "Versão":"1.0"}