# Guia de estudos: FastAPI

Este arquivo reúne os comandos básicos para executar uma aplicação FastAPI e uma explicação das bibliotecas usadas para desenvolver uma API com banco de dados e autenticação.

## 1. Como executar o FastAPI

### 1.1. Acesse a pasta do projeto

No terminal, entre na pasta do projeto. Substitua o caminho de exemplo pelo caminho real da sua pasta:

```bash
cd ~/Desktop/cursos/fast-api
```

### 1.2. Ative o ambiente virtual

No Git Bash do Windows, se o ambiente virtual foi criado na pasta `.venv`, execute:

```bash
source .venv/Scripts/activate
```

Quando o ambiente estiver ativo, normalmente aparece `(.venv)` no início da linha do terminal.

Se ainda não criou o ambiente virtual, execute uma vez, dentro da pasta do projeto:

```bash
python -m venv .venv
```

Depois, ative-o com o comando acima.

### 1.3. Instale as dependências

Com o ambiente virtual ativo, instale os pacotes necessários para este guia:

```bash
python -m pip install fastapi uvicorn sqlalchemy "passlib[bcrypt]" "python-jose[cryptography]" python-dotenv python-multipart
```

Se o curso fornecer um arquivo `requirements.txt`, prefira instalar as dependências definidas nele:

```bash
python -m pip install -r requirements.txt
```

### 1.4. Execute a aplicação

Se o arquivo se chama `main.py` e dentro dele existe uma variável `app` que contém a aplicação FastAPI, execute:

```bash
python -m uvicorn main:app --reload
```

O comando também pode ser escrito como `uvicorn main:app --reload`, desde que o Uvicorn esteja disponível no ambiente ativo.

#### O que significa `uvicorn main:app --reload`?

1. **`uvicorn`** — é o servidor ASGI que executa a aplicação e recebe requisições HTTP.
2. **`main`** — é o nome do arquivo Python `main.py`, sem a extensão `.py`.
3. **`:app`** — indica o nome da variável dentro de `main.py` que contém a instância da aplicação FastAPI.
4. **`--reload`** — reinicia o servidor automaticamente quando detecta alterações nos arquivos monitorados. É útil durante o desenvolvimento.

Exemplo de conteúdo para `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Olá, FastAPI!"}
```

Neste exemplo, `app` é a instância da aplicação, por isso o comando usa `main:app`.

### 1.5. Acesse a API

Com o servidor em execução, abra no navegador:

- **API:** http://127.0.0.1:8000
- **Documentação Swagger:** http://127.0.0.1:8000/docs
- **Documentação alternativa (ReDoc):** http://127.0.0.1:8000/redoc

### 1.6. Encerre a execução

- Para parar o servidor, pressione `Ctrl + C` no terminal.
- Para desativar o ambiente virtual, execute:

```bash
deactivate
```

> **Se o Uvicorn não for encontrado:** confirme se o ambiente virtual está ativo e execute `python -m uvicorn main:app --reload`. Se o pacote não estiver instalado nesse ambiente, instale-o com `python -m pip install uvicorn`.

---

## 2. Bibliotecas usadas no projeto

Essas bibliotecas podem ser usadas para construir uma API com FastAPI, conectar ao banco de dados, proteger senhas, implementar autenticação e gerenciar configurações.

### 2.1. `fastapi`

É o framework usado para criar a API em Python. Permite definir rotas, receber dados, validar requisições e retornar respostas.

**Exemplo:** criar um endpoint para cadastrar usuários.

### 2.2. `uvicorn`

É o servidor ASGI que executa a aplicação FastAPI e disponibiliza os endpoints para receber requisições HTTP.

**Exemplo:** iniciar o servidor com `python -m uvicorn main:app --reload`.

### 2.3. `sqlalchemy`

É uma biblioteca para trabalhar com bancos de dados SQL, como PostgreSQL, MySQL e SQLite. Permite consultar registros, inserir dados, atualizar informações e, usando o ORM, mapear tabelas para classes Python.

**Exemplo:** salvar um usuário no banco de dados.

> O SQLAlchemy não instala automaticamente o driver de todos os bancos. Dependendo do banco escolhido, pode ser necessário instalar um pacote adicional, como `psycopg` para PostgreSQL ou `pymysql` para MySQL.

### 2.4. `passlib[bcrypt]`

O Passlib facilita o armazenamento de senhas por meio de hashes. O `bcrypt` é um algoritmo que pode ser utilizado nesse processo.

**Exemplo:** armazenar o hash de uma senha em vez da senha original.

**Importante:** não se deve armazenar senhas em texto puro. A senha original não é recuperada diretamente a partir do hash; durante o login, a senha informada é verificada contra o hash armazenado.

> **Atenção:** Passlib pode apresentar questões de compatibilidade com versões recentes de dependências. Para um projeto novo, verifique se a biblioteca é compatível com as versões usadas no curso ou considere uma alternativa mantida atualmente. Se estiver seguindo um curso, mantenha as versões recomendadas por ele para evitar diferenças no ambiente.

### 2.5. `python-jose[cryptography]`

Permite trabalhar com tokens, como JWT (_JSON Web Tokens_), frequentemente usados na autenticação de APIs.

**Exemplo:** após o login, a API pode emitir um token que o cliente envia nas próximas requisições.

O extra `[cryptography]` instala suporte criptográfico para os recursos disponibilizados pela biblioteca.

> **Atenção:** valide a manutenção e a compatibilidade da biblioteca antes de adotá-la em um projeto novo. Siga as versões indicadas pelo curso caso esteja reproduzindo o ambiente das aulas.

### 2.6. `python-dotenv`

Permite carregar variáveis de configuração de um arquivo `.env` para o ambiente Python.

**Exemplo:** configurar a URL do banco de dados e a chave secreta usada na autenticação sem deixar esses valores diretamente no código.

**Segurança:** não envie seu arquivo `.env` para o GitHub se ele contiver senhas, chaves ou outros segredos. Adicione `.env` ao `.gitignore` e, se necessário, mantenha um arquivo `.env.example` com nomes de variáveis e valores fictícios.

### 2.7. `python-multipart`

Permite que o FastAPI processe requisições com dados no formato `multipart/form-data`.

É útil para formulários HTML, envio de arquivos e endpoints que recebem campos de formulário, por exemplo, um login com `OAuth2PasswordRequestForm`.

---

## 3. Como instalar as bibliotecas

Se você já criou e ativou o ambiente virtual `.venv`, execute no terminal:

```bash
python -m pip install fastapi uvicorn sqlalchemy "passlib[bcrypt]" "python-jose[cryptography]" python-dotenv python-multipart
```

As aspas nos pacotes que contêm colchetes ajudam a evitar problemas com o shell.

Para confirmar que o FastAPI e o Uvicorn estão instalados no Python ativo:

```bash
python -m pip show fastapi uvicorn
```

### Salvar as dependências do projeto

Depois de instalar os pacotes necessários, você pode registrar as versões instaladas:

```bash
python -m pip freeze > requirements.txt
```

Em outro ambiente, as dependências podem ser instaladas com:

```bash
python -m pip install -r requirements.txt
```

> Gere o `requirements.txt` com o ambiente virtual correto ativado, para não registrar por engano pacotes de outro projeto.

---

## 4. Como as bibliotecas trabalham juntas?

Imagine que você está desenvolvendo uma API de cadastro e login de usuários:

| Biblioteca                  | Função                                                        |
| --------------------------- | ------------------------------------------------------------- |
| `fastapi`                   | Define rotas, valida dados e organiza a API                   |
| `uvicorn`                   | Executa a aplicação e recebe requisições HTTP                 |
| `sqlalchemy`                | Consulta e grava dados no banco de dados                      |
| `passlib[bcrypt]`           | Gera e verifica hashes de senhas, se adotado pelo projeto     |
| `python-jose[cryptography]` | Trabalha com tokens JWT, se adotado pelo projeto              |
| `python-dotenv`             | Carrega configurações a partir de um arquivo `.env`           |
| `python-multipart`          | Processa formulários e uploads que usam `multipart/form-data` |

---

## 5. Preciso instalar todas?

Depende das funcionalidades do projeto.

| Biblioteca                  | Quando é necessária                                                        |
| --------------------------- | -------------------------------------------------------------------------- |
| `fastapi`                   | Para criar a API                                                           |
| `uvicorn`                   | Para executar o servidor localmente ou em uma configuração ASGI compatível |
| `sqlalchemy`                | Se o projeto usar SQLAlchemy para acessar o banco                          |
| `passlib[bcrypt]`           | Se o projeto usar Passlib com bcrypt para proteger senhas                  |
| `python-jose[cryptography]` | Se o projeto usar essa biblioteca para trabalhar com JWT                   |
| `python-dotenv`             | Se o projeto precisar carregar configurações de um arquivo `.env`          |
| `python-multipart`          | Se houver formulários ou uploads que dependam de `multipart/form-data`     |

Se estiver acompanhando um curso que usa exatamente essas bibliotecas, instale as versões previstas pelo curso. Isso reduz o risco de diferenças entre o código das aulas e o seu ambiente.

## 6. Fluxo rápido para o dia a dia

Sempre que for trabalhar no projeto:

1. Abra o terminal.
2. Entre na pasta do projeto.
3. Ative o ambiente virtual.
4. Inicie o servidor.
5. Teste a API em `/docs`.
6. Quando terminar, pare o servidor com `Ctrl + C` e, se desejar, desative o ambiente virtual.

```bash
cd ~/Desktop/cursos/fast-api
source .venv/Scripts/activate
python -m uvicorn main:app --reload
```
