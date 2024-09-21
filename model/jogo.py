from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON  # Importa o tipo JSON específico do PostgreSQL
from model import Base

class Jogo(Base):
    __tablename__ = 'jogo'

    id = Column("pk_jogo", Integer, primary_key=True)
    modalidade = Column(String)
    numeros = Column(JSON, unique=True)  # Usando o tipo JSON do PostgreSQL para trabalhar com listas

    def __init__(self, modalidade: str, numeros: list):
        """
        Cria um Jogo

        Arguments:
            modalidade: modalidade do jogo
            numeros: lista de números associados ao jogo
        """
        self.modalidade = modalidade
        self.numeros = numeros
      
