from fastapi import APIRouter, HTTPException, status
from schemas.aluno import AlunoEntrada, AlunoResposta, AlunoPatch
from database import SessionLocal
from models.aluno import Aluno
from models.curso import Curso
from utils.utils import obter_ou_404
from excecoes import RecursoNaoEncontrado

router = APIRouter(prefix="/alunos", tags=["Alunos"])


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
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise RecursoNaoEncontrado("Aluno")
        return aluno

    
#----------------POST----------------
@router.post("", 
            response_model=AlunoResposta, status_code=201)
def criar_aluno(dados: AlunoEntrada):
    with SessionLocal() as session:
        curso = session.get(Curso, dados.curso_id)
        if curso is None:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "Curso informado não encontrado")
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
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado!")
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
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="Aluno não encontrado!")
        mudancas = dados.model_dump(exclude_unset=True) 
        for campo, valor in mudancas.item():
            setattr(aluno, campo, valor)
        session.commit()
        return aluno 


#-------------DELETE-----------------
@router.delete("/{aluno_id}",
                status_code=status.HTTP_204_NO_CONTENT)
def remover_aluno(aluno_id: int):
    with SessionLocal() as session:
        aluno = session.get(Aluno, aluno_id)
        if aluno is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail="Aluno não encontrado!")
        session.delete(aluno)
        session.commit()