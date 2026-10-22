# Estudos de FastAPI — Introdução ao SQLAlchemy e SQLite

## 1. O que é SQLAlchemy?

O **SQLAlchemy** é uma biblioteca Python que facilita a comunicação com bancos de dados. Ele permite trabalhar com tabelas e registros utilizando classes e objetos Python, sem precisar escrever todas as consultas SQL manualmente.

Ele utiliza uma técnica chamada **ORM (Object-Relational Mapping)**, que relaciona objetos Python às tabelas do banco de dados.

Por exemplo:

- Uma classe Python representa uma tabela.
- Um atributo da classe representa uma coluna.
- Um objeto da classe representa um registro da tabela.

**Neste projeto, utilizaremos o SQLite**, um banco de dados leve que armazena os dados em um arquivo local, sem precisar instalar ou configurar um servidor de banco de dados.

## 2. Importando as ferramentas

```python
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
```

O que cada importação faz?

- `create_engine`: cria a conexão com o banco de dados.
- `Column`: define as colunas de uma tabela.
- `ForeignKey`: estabelece uma referência entre colunas de tabelas diferentes.
- `declarative_base`: cria a classe base utilizada para declarar os modelos do banco.

## 3. Criando a conexão com o banco

```python
from sqlalchemy import create_engine

db = create_engine("sqlite:///banco.db")
```

- `create_engine()` configura o acesso ao banco de dados.
- `sqlite:///banco.db` indica que será utilizado um banco SQLite chamado `banco.db`, armazenado localmente.

O objeto `db` será utilizado para interagir com o banco.

**Importante:** criar o `engine` não cria automaticamente as tabelas. Isso será feito posteriormente.

## 4. Criando a base dos modelos

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

A variável `Base` é a classe base que os modelos herdarão.

Ela permite que o SQLAlchemy reconheça as classes que representam tabelas e reúna suas informações para a criação da estrutura do banco de dados.

## 5. Criando a tabela de usuários

```python
from sqlalchemy import Column, String, Integer, Boolean

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String, nullable=False)
    senha = Column(String)
    ativo = Column(Boolean)
    admin = Column(Boolean, default=False)
```

### Entendendo cada parte

- `class Usuario(Base)`: declara um modelo chamado `Usuario`, que herda a estrutura do SQLAlchemy.
- `__tablename__ = "usuarios"`: define o nome da tabela no banco.
- `id`: identifica cada usuário.
- `primary_key=True`: define a chave primária, utilizada para identificar unicamente cada registro.
- `autoincrement=True`: permite incrementar automaticamente o identificador numérico.
- `nome`: armazena o nome do usuário.
- `email`: armazena o e-mail.
- `nullable=False`: impede que o campo seja salvo como `NULL`.
- `senha`: armazena o campo destinado à senha.
- `ativo`: indica se o usuário está ativo.
- `admin`: indica se o usuário possui perfil administrativo.
- `default=False`: define `False` como valor padrão de `admin` quando nenhum outro valor é fornecido.

**Atenção:** `nullable=False` impede valores nulos, mas não impede uma string vazia. Além disso, senhas reais devem ser armazenadas como hashes seguros, nunca em texto puro.

## 6. Criando o método construtor

```python
def __init__(self, nome, email, senha, ativo, admin):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.ativo = ativo
    self.admin = admin
```

O método `__init__()` é executado quando um novo objeto da classe é criado.

- `self`: representa o próprio objeto.
- `nome`, `email`, `senha`, `ativo` e `admin`: são os valores recebidos na criação.
- `self.nome = nome`: atribui o valor recebido ao atributo do objeto.

Exemplo:

```python
usuario = Usuario(
    nome="Maria",
    email="maria@email.com",
    senha="hash_da_senha",
    ativo=True,
    admin=False
)
```

Esse código cria um objeto Python. **Ele ainda não salva o usuário no banco de dados.** Para isso, será necessário utilizar uma sessão do SQLAlchemy.
