from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, schemas, models
from ..repository import user
from sqlalchemy.orm import Session


get_db = database.get_db
router = APIRouter(
    prefix= '/user',
    tags= ['users']
)



@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(db, request)

@router.get('/{id}', response_model= schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(db, id)

