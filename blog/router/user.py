from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, schemas, models
from ..repository import user
from sqlalchemy.orm import Session


get_db = database.get_db
router = APIRouter(
    prefix= '/user',
    tags= ['users']
)

@router.post('/', response_model=schemas.User)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(db, request)

@router.get('/{id}', response_model= schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(db, id)


@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all_users(db)

@router.put('/{id}')
def update_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    return user.update_user(db, request, id)

@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return user.delete_user(db, id)
