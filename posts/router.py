from posts.schemas import CreatePostRequest, EditPostRequest, GeneratePostRequest
from fastapi import HTTPException, APIRouter
from posts import service
import os
import requests


router = APIRouter()




@router.get('/posts')
async def get_posts():
    return await service.get_posts()


@router.post('/posts')
async def create_post(post: CreatePostRequest):
    return await service.create_post(post)


@router.get('/posts/{post_id}')
async def get_post(id: int):
    return await service.get_post_by_id(id)


@router.put('/posts/{post_id}')
async def edit_post(id: int, post_data: EditPostRequest):
    return await service.edit_post(id, post_data)


@router.delete('/posts/{post_id}')
async def delete_post(id: int):
    await service.delete_post(id)

    return {"message": "ok, deleted"}
    
@router.post('/posts/generate-ad-text')
def genenerate_ad(request: GeneratePostRequest):

    token = os.environ.get("TOKEN")

    headers = {
        'Authorization': "Bearer " + token
    }

    response = requests.post('https://7583-185-48-148-173.ngrok-free.app/custom-prompt', headers=headers, json={
        "input_text": "generate mental health support text that cheers up the user, starting with words 'Hi, I am Barbie!' based on these keywords: "  +  request.keywords
    })

    body = response.json()
    return {
        "text": body['output']
    }
    






