# Minha API

JOGOS LOTERIA

Esta API faz parte do projeto MVP desenvolvido para a disciplina de Full-Stack Básico da PUC-RIO.
O projeto, ainda em fase inicial, é uma aplicação para gerar jogos da loteria.

Demonstração da configuração banco de dados e da utilização das 3 rotas abaixo:
- método GET - busca a lista de itens da base de dados
- método DELETE - deleta um item da base de dados
- método POST -  adiciona um item na base de dados

---

## Usuários iniciantes - WINDOWS 

Primeiro instale o VSCODE e clone este repositório em seu workspace.
É necessário instalar a linquagem Python, pode ser baixado na microsoft store.
Durante o desenvolvimento desta aplicação foi utilizado Python==3.12

## Como executar 

DICA WINDOWS: Após instalação da linguagem python, abra o terminal no VSCODE e execute o comando abaixo para instalar o 
virtual environment (venv) na pasta de destino.

```
pyhton -m venv [Nome Da Pasta]
```

Próximo passo é ativar o virtual environment, entre na diretório Scripts e execute `activate`. 
Se estiver aparecendo (venv) em frente a letra da unidade no terminal, sucesso.

## Bibliotecas
Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, execute o comando abaixo no diretório raiz,
este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`. 

```
pip install -r requirements.txt 
```

## Execução API
Para executar a API basta executar no diretório raiz:

```
flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.