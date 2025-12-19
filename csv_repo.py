import csv
from pathlib import Path
from core.entities import Order
from core.ports import OrderRepository

class CSVOrderRepository(OrderRepository):
    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)
        self.csv_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.csv_path.exists():
            with open(self.csv_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "sku", "qty"])

    def create(self, order: Order) -> str:
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([order.id, order.sku, order.qty])
        return order.id

    def get_by_id(self, order_id: str):
        with open(self.csv_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["id"] == order_id:
                    return Order(id=row["id"], sku=row["sku"], qty=int(row["qty"]))
        return None
