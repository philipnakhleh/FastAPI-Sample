from pydantic import BaseModel
from datetime import date
from typing import List


class Blog(BaseModel):
    blog_title : str
    blog_description : str
    blog_date : date
    blog_summarization : str
    blog_writer : str
    blog_reviewer : str
    blog_cover_pic: str

    class Config:
        orm_mode = True

class Show_in_Blogs_Page(BaseModel):
    blog_title: str
    blog_summarization: str
    blog_date: date
    id: int
    blog_cover_pic: str

    class Config:
        orm_mode = True

class Show_Blog(BaseModel):
    blog_title: str
    blog_date: date
    blog_description: str
    blog_writer: str
    blog_reviewer: str
    blog_cover_pic: str

    class Config:
        orm_mode = True

class Show_Blog2(BaseModel):
    data: List[Show_in_Blogs_Page]

    class Config:
        orm_mode = True