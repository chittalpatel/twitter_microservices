import os


class Config:
    USE_POSTGRES = os.getenv("USE_POSTGRES") == "true"

    pg_db = os.getenv("POSTGRES_DB")
    pg_user = os.getenv("POSTGRES_USER")
    pg_password = os.getenv("POSTGRES_PASSWORD")
    pg_host = os.getenv("DATABASE_URL")
    if USE_POSTGRES and (not pg_db or not pg_user or not pg_password or not pg_host):
        raise ValueError("POSTGRES not configured")

    POSTGRES_URL = f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}"
