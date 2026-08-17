from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Curso(Base):
    __tablename__ = "cursos" #nome da tabela (nome da tabela sempre no plural)

    id: Mapped[int] = mapped_column(primary_key=True) # PK
    nome: Mapped[str]
    carga_horaria: Mapped[int]
    alunos: Mapped[list["Aluno"]] = relationship(back_populates="cursos")