from .entities import Order
from .ports import OrderRepository
from .errors import ValidationError

class CreateOrder:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, sku: str, qty: int) -> str:
        if not sku.strip():
            raise ValidationError("SKU cannot be empty")
        if qty <= 0:
            raise ValidationError("Quantity must be > 0")
        order = Order(sku=sku, qty=qty)
        return self.repo.create(order)

class GetOrder:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, order_id: str):
        order = self.repo.get_by_id(order_id)
        if not order:
            return None
        return order
