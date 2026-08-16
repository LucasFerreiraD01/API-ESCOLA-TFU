from database import SessionLocal
from models.aluno import Aluno

session = SessionLocal()

alunos = session.query(Aluno).all() #essa linha significa "vá na tabela de alunos e me traga todas a linhas disponiveis"
for a in alunos:
    print(a.id, a.nome, a.idade)

session.close()
