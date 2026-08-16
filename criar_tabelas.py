from database import Base, engine
import models.aluno

Base.metadata.create_all(bind=engine) #cria tudo dentro do banco oq é descendente de Base, mas antes de criar, vê se ela existe.

