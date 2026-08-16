from database import SessionLocal
from models.aluno import Aluno

session = SessionLocal() #abriu a sessao

novo = Aluno(nome="Ana Souza", idade=20) #criou o objeto aluno
session.add(novo) #coloca a ana souza na fila
session.commit() # grava e confirma o objeto (ana souza) no banco

print(novo.id)
session.close()
