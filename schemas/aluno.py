#schema (pydantic) é como o dado ENTRA e SAI da API (schemas/aluno.py, herdade BaseModel) (isso que é a validaçao)

from pydantic import BaseModel, Field, ConfigDict

class AlunoEntrada(BaseModel):
    nome: str = Field(min_length=3)
    idade: int = Field(ge=16)
    ativo: bool = True


class AlunoResposta(BaseModel):
    model_config = ConfigDict(from_atributes=True)
    id:int
    nome:str
    idade:int
    ativo:bool

class AlunoPach(BaseModel):
    nome: str | None = Field(default=None, min_length=3)
    idade: int | None = Field(default=None, ge=16)
    ativo: bool| None = None