from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field

alunos = [
{"id": 1, "nome": "Ana Souza","idade": 25, "ativo": True},
{"id": 2, "nome": "Bruno Lima","idade": 29, "ativo": True},
{"id": 3, "nome": "Carla Dias","idade": 22, "ativo": False},
]

app = FastAPI()

class AlunoEntrada(BaseModel):
    nome: str = Field(min_length=3)
    idade: int = Field(ge=16)
    ativo: bool = True


class AlunoResposta(BaseModel):
    id:int
    nome:str
    idade:int
    ativo:bool

class AlunoPach(BaseModel):
    nome: str | None = Field(default=None, min_length=3)
    idade: int | None = Field(default=None, ge=16)
    ativo: bool| None = None

#----------------GET----------------
@app.get("/")

def raiz():
    return {"Mensagem": "API da Escola no ar!"}

@app.get ("/status")
def status():
    return{"Status":"OK", "Versão":"1.0"}

@app.get("/alunos", response_model=list[AlunoResposta])
def listar_alunos(ativo:bool| None = None, limite: int=10):
    resultado = alunos 
    if ativo is not None:
        resultado = [a for a in resultado
                    if a ["ativo"]==ativo]
    return resultado[:limite]

@app.get("/alunos/{aluno_id}", response_model=AlunoResposta)
def buscar_aluno(aluno_id:int):
    for aluno in alunos:
        if aluno["id"]==aluno_id:
            return aluno
        raise HTTPException(status_code=404, detail= "Aluno não encontrado!")
    
#----------------POST----------------
@app.post("/alunos",status_code=201)
def criar_aluno(aluno: AlunoEntrada):
    novo = aluno.model_dump()
    novo["id"] = max([a["id"] for a in aluno ], default=0)+1
    alunos.append(aluno)
    return aluno

#----------------PUT-------------------
@app.put("/alunos/{aluno_id}")
def atualizar_aluno(aluno_id: int, dados: AlunoEntrada):
    for indice, aluno in enumerate(alunos):
        if aluno["id"] == aluno_id:
            atualizado = dados.model_dump()
            atualizado["id"] = aluno_id
            alunos[indice] = atualizado 
            return dados
    raise HTTPException(status_code=404,detail="Aluno nao encontrado")

#--------------PATCH----------------
@app.patch("/alunos/{aluno_id}")
def alterar_aluno(aluno_id: int, dados: AlunoPach):
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            mudancas = dados.model_dump(exclude_unset=True)
            aluno.update(mudancas)
            return aluno
    raise HTTPException(status_code=404,detail="Aluno nao encontrado")

#-------------DELETE-----------------
@app.delete("/alunos/{aluno_id}")
def remover_aluno(aluno_id: int):
    for indice, aluno in enumerate(alunos):
        if aluno["id"] == aluno_id:
            alunos.pop(indice)
            return {"mensagem": "Aluno removido"}
    raise HTTPException(status_code=404,detail="Aluno nao encontrado")