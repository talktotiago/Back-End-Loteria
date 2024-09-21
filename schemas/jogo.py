from pydantic import BaseModel
from typing import List
from model.jogo import Jogo


class JogoSchema(BaseModel):
    """ Define como um novo jogo a ser inserido deve ser representado
    """
    modalidade: str = "Mega-Sena"
    numeros: list = [1, 4, 6, 7, 22, 26]

class JogoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do jogo
    """
    id: int = 1

class JogoBuscaModelSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do jogo
    """
    modalidade: str = "Mega-Sena"

class ListagemJogosSchema(BaseModel):
    """ Define como uma listagem de jogos será retornada.
    """
    jogos:List[JogoSchema]

class JogoViewSchema(BaseModel):
    """ Define como um jogo será retornado
    """
    id: int = 1
    modalidade: str = "Mega-Sena"
    numeros: list = [1, 4, 23, 32, 47, 60]

def apresenta_jogo(jogo: Jogo):
    """ Retorna uma representação do jogo seguindo o schema definido em
        JogoViewSchema.
    """
    return {
        "id": jogo.id,
        "modalidade": jogo.modalidade,
        "numeros": jogo.numeros,
    }

def apresenta_jogos(jogos: List[Jogo]):
    """ Retorna uma representação do jogo seguindo o schema definido em
        JogoViewSchema.
    """
    result = []
    for jogo in jogos:
        result.append({
            "id": jogo.id,
            "modalidade": jogo.modalidade,
            "numeros": jogo.numeros,
        })
    return {"jogos": result}  

class JogoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    id: int
    mesage: str
    numeros: list
