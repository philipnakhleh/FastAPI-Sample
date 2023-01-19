from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from typing import List
from ..database import get_db
from ..repository import buyer

router = APIRouter(
    prefix= '/buyer',
    tags= ['buyer']
)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return buyer.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Buyer, db: Session = Depends(get_db)):
    return buyer.create(db, request)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id, db: Session = Depends(get_db)):
    return buyer.delete(db, id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_buyer(id, request: schemas.Buyer, db: Session = Depends(get_db)):
    return buyer.update_buyer(db, request, id)

@router.get('/{id}', status_code=200)
def show(id, db: Session = Depends(get_db)):
    return buyer.get_id(db, id)

