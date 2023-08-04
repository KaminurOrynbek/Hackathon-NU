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

DATABASE_URL = "postgresql://barbie:barbie@127.0.0.1:5432/barbie"

database = Database(DATABASE_URL)
metadata = MetaData()

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("username", String, unique = True),
    Column("keywords", String),
    Column("text", Text),
    Column("created_at", DateTime, server_default=func.now()),
)

engine = create_engine(DATABASE_URL)

metadata.create_all(engine)
