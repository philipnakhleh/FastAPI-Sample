from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import blogs_schemas, models
from typing import List
from ..database import get_db
from ..repository import blogs
import math, random



router = APIRouter(
    prefix= '/blogs',
    tags= ['blogs']
)


@router.get('/', response_model= blogs_schemas.Show_Blog2)
def all(db: Session = Depends(get_db)):
    return {
        'data' : blogs.get_list(db)
    }


@router.get('/{id}', status_code=200, response_model= blogs_schemas.Show_Blog)
def show(id, db: Session = Depends(get_db)):
    return blogs.get_id(db, id)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: blogs_schemas.Blog, db: Session = Depends(get_db)):
    return blogs.create(db, request)