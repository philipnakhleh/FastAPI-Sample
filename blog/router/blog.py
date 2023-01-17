from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from typing import List
from ..database import get_db
from ..repository import blog

router = APIRouter(
    prefix= '/blog',
    tags= ['blogs']
)


@router.get('/', response_model=List[schemas .ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogBase, db: Session = Depends(get_db)):
    return blog.create(db, request)



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.delete(db, id)



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.BlogBase, db: Session = Depends(get_db)):
    return blog.update(db, request, id)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return blog.get_id(db, id)

