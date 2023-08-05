from typing import Optional
from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    username: str
    keywords: str
    text: str


class EditPostRequest(BaseModel):
    username: Optional[str] = None
    keywords: Optional[str] = None
    text: Optional[str] = None