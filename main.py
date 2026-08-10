from fastapi import FastAPI
from routers import alunos,cursos

app = FastAPI(title="API - SENAI", tags= ["Status da Aplicação"])

app.include_router(alunos.router)
app.include_router(cursos.router)

@app.get("")
def raiz():
    return {"Mensagem": "API da Escola no ar!"}

@app.get ("/status")
def status():
    return{"Status":"OK", "Versão":"1.0"}
