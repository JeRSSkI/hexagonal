from fastapi import APIRouter, HTTPException
from core.usecases import CreateOrder, GetOrder

def setup_routes(repo):
    router = APIRouter()
    create_uc = CreateOrder(repo)
    get_uc = GetOrder(repo)

    @router.post("/orders", status_code=201)
    async def create_order(dto: dict):
        try:
            order_id = create_uc.execute(dto["sku"], dto["qty"])
            return {"id": order_id}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.get("/orders/{order_id}")
    async def get_order(order_id: str):
        order = get_uc.execute(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order.dict()

    return router
