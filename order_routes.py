from fastapi import APIRouter

#roteador
order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def order():
  """
  Essa é a rota padrão de pedidos do nosso sistema. Para todas as rotas de pedidos o usuário precisa estar autenticado.
  """
  return {"mensagem": "você acessou a rota de pedidos"}