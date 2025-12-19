import asyncpg
from core.entities import Order
from core.ports import OrderRepository

class PostgresOrderRepository(OrderRepository):
    def __init__(self, pool):
        self.pool = pool

    async def create(self, order: Order) -> str:
        async with self.pool.acquire() as conn:
            await conn.execute(
                "INSERT INTO orders(id, sku, qty) VALUES($1, $2, $3)",
                order.id, order.sku, order.qty
            )
        return order.id

    async def get_by_id(self, order_id: str):
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT id, sku, qty FROM orders WHERE id=$1", order_id
            )
            if row:
                return Order(**row)
            return None
