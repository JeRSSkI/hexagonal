import os
from adapters.db.postgres_repo import PostgresOrderRepository
from adapters.file.csv_repo import CSVOrderRepository
import asyncpg

def get_repo_adapter():
    adapter_type = os.getenv("REPO_ADAPTER", "db")
    if adapter_type == "file":
        return CSVOrderRepository(os.getenv("CSV_PATH", "/data/orders.csv"))
    else:
        # Postgres
        pool = asyncpg.create_pool(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 5432)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        return PostgresOrderRepository(pool)
