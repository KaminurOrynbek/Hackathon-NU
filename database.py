from databases import Database
from sqlalchemy import (
    MetaData, 
    create_engine, 
    Table, 
    Column, 
    Integer,
    Identity,
    String,
    Text,
    DateTime,
    func
)

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"

database = Database(DATABASE_URL)
metadata = MetaData()

stories = Table(
    "stories",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("username", String, unique = True),
    Column("text", Text),
    Column("keywords", String),
    Column("created_at", DateTime, server_default=func.now()),
)

engine = create_engine(DATABASE_URL)

metadata.create_all(engine)