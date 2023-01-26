from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import blogs_models, blogs_schemas

def get_list(db: Session):
    buyers = db.query(blogs_models.Blog).all()
    return buyers


def create(db: Session, request: blogs_schemas.Blog):
    new_blog = blogs_models.Blog(
        blog_title= request.blog_title,
        blog_description = request.blog_description,
        blog_writer = request.blog_writer,
        blog_date = request.blog_date,
        blog_summarization = request.blog_summarization,
        blog_reviewer = request.blog_reviewer
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        'message' : 'Blog_Added'
    }



def get_id(db: Session, id):
    blog = db.query(blogs_models.Blog).filter(blogs_models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return blog
