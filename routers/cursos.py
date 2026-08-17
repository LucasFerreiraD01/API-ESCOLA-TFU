#routers/curso.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import selectinload
from schemas.curso import CursoEntrada, CursoResposta, CursoComAlunos
from database import SessionLocal
from models.curso import Curso

router = APIRouter(prefix="/cursos", tags=["Cursos"])

cursos = [
    {"id":1, "nome": "Python Back-End", "carga_horaria": 180},
    {"id":2, "nome": "Banco de Dados", "carga_horaria": 200},
    {"id":3, "nome": "Front End", "carga_horaria": 150},
    {"id":4, "nome": "Analise de Dados", "carga_horaria": 90},
]

@router.get("", response_model=list[CursoResposta])
def listar_cursos():
    with SessionLocal() as session:
        return session.query(Curso).all()

@router.get("/{curso_id}", response_model=CursoComAlunos)
def buscar_curso(curso_id: int):
    with SessionLocal() as session: 
        curso = session.query(Curso).opitions(selectinload(Curso.alunos)).get(curso_id)
        if curso is None:
            raise HTTPException(status_code=400, detail="Curso não encontrado!")
        return curso

@router.post("", response_model=CursoResposta,
            status_code=201)
def criar_cursos(dados: CursoEntrada):
    with SessionLocal() as session:
        curso = Curso(**dados.model_dump())
        session.add(curso)
        session.commit()
        return curso