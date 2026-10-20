# CRUD e REST API com FastAPI

## 1. O que é CRUD?

CRUD representa as quatro operações básicas realizadas em dados de uma aplicação:

- **C — Create:** criar um registro.
- **R — Read:** ler ou consultar um registro.
- **U — Update:** atualizar um registro.
- **D — Delete:** excluir um registro.

## 2. Métodos HTTP de uma REST API

Em uma REST API, utilizamos métodos HTTP para definir o tipo de operação que será executada.

| Método HTTP | Operação | Descrição                            |
| ----------- | -------- | ------------------------------------ |
| `GET`       | Read     | Consultar ou obter dados.            |
| `POST`      | Create   | Enviar dados para criar um registro. |
| `PUT`       | Update   | Substituir completamente um recurso. |
| `PATCH`     | Update   | Atualizar parcialmente um recurso.   |
| `DELETE`    | Delete   | Excluir um registro.                 |

## 3. Organização dos arquivos e rotas

É importante organizar as rotas em arquivos separados, em vez de colocar todas elas diretamente no `main.py`.

Uma estrutura básica pode ser:

```text
meu_projeto/
├── main.py
├── requirements.txt
└── routes/
    ├── __init__.py
    └── usuarios.py
```

- `main.py`: cria a aplicação FastAPI e registra as rotas.
- `routes/`: diretório que contém os arquivos de rotas.
- `usuarios.py`: define as rotas relacionadas aos usuários.
- `__init__.py`: permite organizar o diretório como um pacote Python.

## 4. Ordem de importação no `main.py`

A ordem de execução é importante porque, antes de registrar as rotas, precisamos ter uma instância da aplicação FastAPI.

Primeiro, criamos o `app`. Depois, importamos ou registramos os módulos de rotas e incluímos seus roteadores na aplicação.

### Exemplo de `main.py`

```python
from fastapi import FastAPI
from routes.usuarios import router as usuarios_router

app = FastAPI()

app.include_router(usuarios_router)
```

**Atenção:** no Python, os imports são executados na ordem em que aparecem. O módulo `routes.usuarios` é carregado antes da execução de `app = FastAPI()`. Por isso, o arquivo de rotas deve apenas definir o roteador, sem depender de uma variável `app` criada no `main.py`. O `include_router()` é executado depois que a aplicação existe.

## 5. Criando o arquivo de rotas

No arquivo `routes/usuarios.py`, definimos um `APIRouter` para agrupar as rotas relacionadas aos usuários.

```python
from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.get("/")
def listar_usuarios():
    return {"mensagem": "Lista de usuários"}


@router.post("/")
def criar_usuario():
    return {"mensagem": "Usuário criado"}


@router.put("/{usuario_id}")
def atualizar_usuario(usuario_id: int):
    return {
        "mensagem": "Usuário substituído",
        "id": usuario_id
    }


@router.patch("/{usuario_id}")
def editar_usuario(usuario_id: int):
    return {
        "mensagem": "Usuário atualizado parcialmente",
        "id": usuario_id
    }


@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int):
    return {
        "mensagem": "Usuário excluído",
        "id": usuario_id
    }
```

Esses exemplos são apenas demonstrativos: ainda não recebem os dados de criação ou edição nem persistem informações em um banco de dados.

## 6. Registrando as rotas na aplicação

A instrução abaixo, no `main.py`, registra todas as rotas definidas no roteador:

```python
app.include_router(usuarios_router)
```

Como o roteador possui o prefixo `/usuarios`, os endpoints ficam assim:

| Método   | Endpoint                 | Finalidade          |
| -------- | ------------------------ | ------------------- |
| `GET`    | `/usuarios/`             | Listar usuários     |
| `POST`   | `/usuarios/`             | Criar usuário       |
| `PUT`    | `/usuarios/{usuario_id}` | Substituir usuário  |
| `PATCH`  | `/usuarios/{usuario_id}` | Editar parcialmente |
| `DELETE` | `/usuarios/{usuario_id}` | Excluir usuário     |

## 7. Testando a API

Execute o servidor:

```bash
python -m uvicorn main:app --reload
```

Acesse a documentação interativa:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

No Swagger, você pode visualizar e testar os métodos HTTP disponíveis.

## Resumo do fluxo

1. Criar a aplicação FastAPI no `main.py`.
2. Criar os arquivos de rotas usando `APIRouter`.
3. Definir os endpoints de cada recurso.
4. Importar os roteadores no `main.py`.
5. Registrar os roteadores com `app.include_router()`.
6. Executar o servidor e testar os endpoints.

**Ideia principal:** o `main.py` centraliza a aplicação, enquanto os arquivos de rotas organizam os endpoints por recurso, deixando o código mais modular e fácil de manter.
