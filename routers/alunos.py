from fastapi import APIRouter, HTTPException
from models.aluno import AlunoEntrada, AlunoResposta, AlunoPach


router = APIRouter(prefix="/alunos", tags=["Alunos"])


alunos = [
{"id": 1, "nome": "Ana Souza","idade": 25, "ativo": True},
{"id": 2, "nome": "Bruno Lima","idade": 29, "ativo": True},
{"id": 3, "nome": "Carla Dias","idade": 22, "ativo": False},
]

#----------------GET----------------
@router.get("",
            response_model=list[AlunoResposta])
def listar_alunos(ativo:bool| None = None, limite: int=10):
    resultado = alunos 
    if ativo is not None:
        filtrados = []
        for a in resultado:
            if a["ativo"] == ativo:
                filtrados.append(a)
            resultado = filtrados
    return resultado[:limite]


@router.get("/{aluno_id}",
            response_model=AlunoResposta)
def buscar_aluno(aluno_id:int):
    for aluno in alunos:
        if aluno["id"]==aluno_id:
            return aluno
        raise HTTPException(status_code=404,
                            detail= "Aluno não encontrado!")
    
#----------------POST----------------
@router.post("",status_code=201)
def criar_aluno(aluno: AlunoEntrada):
    novo = aluno.model_dump()
    novo["id"] = max([a["id"] for a in alunos ], default=0)+1
    alunos.append(novo)
    return novo

#----------------PUT-------------------
@router.put("/{aluno_id}")
def atualizar_aluno(aluno_id: int, dados: AlunoEntrada):
    for indice, aluno in enumerate(alunos):
        if aluno["id"] == aluno_id:
            atualizado = dados.model_dump()
            atualizado["id"] = aluno_id
            alunos[indice] = atualizado 
            return atualizado
    raise HTTPException(status_code=404,detail="Aluno nao encontrado")

#--------------PATCH----------------
@router.patch("/{aluno_id}")
def alterar_aluno(aluno_id: int, dados: AlunoPach):
    for aluno in alunos:
        if aluno["id"] == aluno_id:
            mudancas = dados.model_dump(exclude_unset=True)
            aluno.update(mudancas)
            return aluno
    raise HTTPException(status_code=404,detail="Aluno nao encontrado")

#-------------DELETE-----------------
@router.delete("/{aluno_id}")
def remover_aluno(aluno_id: int):
    for indice, aluno in enumerate(alunos):
        if aluno["id"] == aluno_id:
            alunos.pop(indice)
            return {"mensagem": "Aluno removido"}
    raise HTTPException(status_code=404,
                        detail="Aluno nao encontrado")