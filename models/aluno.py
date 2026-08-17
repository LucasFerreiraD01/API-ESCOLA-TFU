#Model (SQLAlchemy) é como o dado é GUARDADO no banco de dados (models/aluno.py, herda de base) (isso que é a persistencia)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from database import Base
from models.matriculas import matriculas

class Aluno(Base):
    __tablename__ = "alunos" #nome da tabela (nome da tabela sempre no plural)

    id: Mapped[int] = mapped_column(primary_key=True) # PK
    nome: Mapped[str]
    idade: Mapped[int]
    ativo:Mapped[bool] = mapped_column(default=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["Curso"] = relationship(secundary=matriculas, back_populates="alunos")
