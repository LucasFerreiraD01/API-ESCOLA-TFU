from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

#engine = a conexao com o banco (quem "fala" com ele)

#Session = a conversa individual (uma inidade de trabalho)

#Base = a classe-mae de todos os models (todo model vai herdar dela, assim vamos saber oq vai virar tabela ou nao {se herdou de base é tabela, se nao herdou entao nao é})

URL_BANCO = "sqlite:///escola.db"
engine = create_engine(URL_BANCO,
    connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass