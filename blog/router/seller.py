from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from typing import List
from ..database import get_db
from ..repository import seller

router = APIRouter(
    prefix= '/seller',
    tags= ['seller']
)


@router.get('/', response_model=List[schemas.Seller])
def all(db: Session = Depends(get_db)):
    return seller.get_all(db)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Seller, db: Session = Depends(get_db)):
    return seller.create(db, request)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id, db: Session = Depends(get_db)):
    return seller.delete(db, id)



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_seller(id, request: schemas.Seller, db: Session = Depends(get_db)):
    return seller.update_seller(db, request, id)


@router.get('/{id}', status_code=200, response_model=schemas.Seller)
def show(id, db: Session = Depends(get_db)):
    return seller.get_id(db, id)

