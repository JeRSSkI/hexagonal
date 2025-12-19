import pytest
from core.entities import Order
from core.errors import ValidationError

def test_order_invalid_qty():
    from core.usecases import CreateOrder
    class FakeRepo:
        def create(self, order): return order.id

    uc = CreateOrder(FakeRepo())
    import pytest
    with pytest.raises(ValidationError):
        uc.execute("ABC", 0)
