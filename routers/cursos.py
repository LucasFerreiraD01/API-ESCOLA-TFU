#routers/curso.py
from fastapi import APIRouter, HTTPException
from models.curso import CursoEntrada, CursoResposta

router = APIRouter(prefix="/cursos", tags=["Cursos"])

cursos = [
    {"id":1, "nome": "Python Back-End", "carga_horaria": 180},
    {"id":2, "nome": "Banco de Dados", "carga_horaria": 200},
    {"id":3, "nome": "Front End", "carga_horaria": 150},
    {"id":4, "nome": "Analise de Dados", "carga_horaria": 90},
]

@router.get("", response_model=list[CursoResposta])
def listar_cursos():
        return cursos

@router.post("", response_model=CursoResposta,
            status_code=201)
def criar_cursos(curso:CursoEntrada):
    novo = curso.model_dump()
    novo["id"] = max([c["id"] for c in curso], default=0)+1
    curso.append(novo)
    return novo