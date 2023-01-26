from pydantic import BaseModel
from datetime import date


class Blog(BaseModel):
    blog_title : str
    blog_description : str
    blog_date : date
    blog_summarization : str
    blog_writer : str
    blog_reviewer : str

    class Config:
        orm_mode = True

class Show_in_Blogs_Page(BaseModel):
    blog_title: str
    blog_description: str
    blog_date: date

    class Config:
        orm_mode = True

class Show_Blog(BaseModel):
    blog_title: str
    blog_date: date
    blog_summarization: str
    blog_writer: str
    blog_reviewer: str

    class Config:
        orm_mode = True