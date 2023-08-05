from posts.schemas import CreatePostRequest, EditPostRequest
from database import database
from sqlalchemy import insert, select, update, delete
from database import posts
from fastapi import HTTPException

async def create_post(post: CreatePostRequest):
    insert_query = insert(posts).values(
        post.dict()
    ).returning(posts.columns.id)

    return await database.fetch_one(insert_query)

async def get_posts():
    select_query = select(posts)

    return await database.fetch_all(select_query)

async def get_post_by_id(id: int):

    select_by_id = select(posts).where(posts.columns.id == id)
    post =  await database.fetch_one(select_by_id)

    if not post:
        raise HTTPException(status_code = 404, detail = "post is not found")



async def edit_post(post: EditPostRequest, id: int):
