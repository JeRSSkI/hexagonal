from core.entities import Order
from core.usecases import CreateOrder, GetOrder

class FakeRepo:
    def __init__(self):
        self.store = {}

    def create(self, order):
        self.store[order.id] = order
        return order.id

    def get_by_id(self, order_id):
        return self.store.get(order_id)

def test_create_and_get_order():
    repo = FakeRepo()
    create_uc = CreateOrder(repo)
    get_uc = GetOrder(repo)
    order_id = create_uc.execute("ABC", 2)
    order = get_uc.execute(order_id)
    assert order.sku == "ABC"
    assert order.qty == 2
