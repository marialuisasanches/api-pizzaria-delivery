from fastapi import APIRouter 

#roteador
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def auth():

  """
  Essa é a rota padrão de autenticação do sistema 
  """

  return{"mensagem": "você acessou a rota de padrão de autenticação", "autenticado": False}
