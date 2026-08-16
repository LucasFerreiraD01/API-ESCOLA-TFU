from fastapi import APIRouter, HTTPException
from schemas.aluno import AlunoEntrada, AlunoResposta, AlunoPatch
from database import SessionLocal
from models.aluno import Aluno

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
    with SessionLocal() as session:
        query = session.query(Aluno) #consulta na tabela de aluno, mas ela en si n consulta, ela monta o pedido antes de consultar
        if ativo is not None:
            query = query.filter(Aluno.ativo == ativo) 
        return query.limit(limite).all()



@router.get("/{aluno_id}",
            response_model=AlunoResposta)
def buscar_aluno(aluno_id:int):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id) #ta pedindo para a orm buscar dentro da tabela aluno o parametro databela que é o aluno id
        if aluno in None:
            raise HTTPException(status_code=404,
                detail= "Aluno não encontrado!")
        return aluno

    
#----------------POST----------------
@router.post("", 
            response_model=AlunoResposta, status_code=201)
def criar_aluno(dados: AlunoEntrada):
    with SessionLocal() as session:
        aluno = Aluno(**dados.model_dump()) #transforma os dados q recebeu em formato json
        session.add(aluno)
        session.commit()
        return aluno 


#----------------PUT-------------------
@router.put("/{aluno_id}", response_model=AlunoResposta)
def atualizar_aluno(aluno_id: int, dados: AlunoEntrada):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise HTTPException(status_code=404, detail="Aluno não encontrado!")
        aluno.nome = dados.nome
        aluno.idade = dados.idade
        aluno.ativo = dados.ativo
        session.commit()
        return aluno

#--------------PATCH----------------
@router.patch("/{aluno_id}", response_model=AlunoResposta)
def alterar_aluno(aluno_id: int, dados: AlunoPatch):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise HTTPException(status_code=404,
                detail="Aluno não encontrado!")
        mudancas = dados.model_dump(exclude_unset=True)
        for campo, valor in mudancas.item():
            setattr(aluno, campo, valor)
        session.commit()
        return aluno 


#-------------DELETE-----------------
@router.delete("/{aluno_id}")
def remover_aluno(aluno_id: int):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise HTTPException(status_code=404,
                detail="Aluno não encontrado!")
        session.delete(aluno)
        session.commit()
        return {"mensagem": "Aluno removido com sucesso!"}