from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from sqlalchemy.exc import IntegrityError
from model import Session, Jogo
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
jogo_tag = Tag(name="Jogo", description="Adição, visualização e remoção de jogos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/jogo', tags=[jogo_tag],
          responses={"200": JogoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_jogo(form: JogoSchema):
    """Adiciona um novo Jogo à base de dados

    Retorna uma representação dos jogos
    """
    jogo = Jogo(
        modalidade=form.modalidade,
        numeros=form.numeros
        )

    try:
        # criando conexão com a base
        session = Session()
        # adicionando jogo
        session.add(jogo)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_jogo(jogo), 200

    except IntegrityError as e:
        # como a duplicidade do jogo é a provável razão do IntegrityError
        error_msg = "Jogo com mesmos números já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo jogo :/"
        return {"mesage": error_msg}, 400


@app.get('/jogos', tags=[jogo_tag],
         responses={"200": ListagemJogosSchema, "404": ErrorSchema})
def get_jogos():
    """Faz a busca por todos os Jogos cadastrados

    Retorna uma representação da listagem de jogos.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    jogos = session.query(Jogo).all()

    if not jogos:
        msg = "Nenhum jogo cadastrado"
        return {"mesage": msg}, 200
    else:
        # retorna a representação de produto
        print(jogos)
        return apresenta_jogos(jogos), 200


@app.delete('/jogo', tags=[jogo_tag],
         responses={"200": JogoDelSchema, "404": ErrorSchema})
def del_jogo(query: JogoBuscaSchema):
    """Deleta um jogo da base de dados

    Faz a busca do jogo pelo id e depois deleta
    """
    jogo_id = query.id
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    jogo = session.query(Jogo).filter(Jogo.id == jogo_id).delete()
    session.commit()

    if not jogo:
        # se o jogo não foi encontrado
        error_msg = "Jogo não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        return {"mesage": "Produto removido", "id": jogo_id}

'''
@app.get('/modalidade', tags=[jogo_tag],
         responses={"200": JogoViewSchema, "404": ErrorSchema})
def get_modalidade(query: JogoBuscaModelSchema):
    """Faz a busca por jogos com a mesma modalidade

    Retorna uma representação dos produtos e comentários associados.
    """
    jogo_modalidade = query.modalidade
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    jogos = session.query(Jogo).filter(Jogo.modalidade == jogo_modalidade).all()

    if not jogos:
        # se o produto não foi encontrado
        error_msg = "Modalidade não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação de produto
        return apresenta_jogos(jogos), 200
'''      
