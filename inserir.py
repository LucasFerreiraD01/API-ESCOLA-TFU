from database import SessionLocal
from models.aluno import Aluno
from models.curso import Curso

session = SessionLocal() #abriu a sessao

novo_aluno = Aluno(nome="Jorge Antonio", idade=21) #criou o objeto aluno
session.add(novo_aluno) #coloca a ana souza na fila
session.commit() # grava e confirma o objeto (ana souza) no banco


novo_curso = Curso(nome="HTML - Basico", carga_horaria=5)
session.add(novo_curso)
session.commit()


print(novo_aluno.id)
print(novo_curso.id)
session.close()
