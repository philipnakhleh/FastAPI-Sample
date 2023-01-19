from sqlalchemy.orm import Session
from .. import models, schemas
from ..Hashing import Hash
from fastapi import status, HTTPException

def create_user(db: Session, request : schemas.User):
    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        birthday=request.birthday,
        email=request.email,
        phone=request.phone,
        organization_name=request.organization_name,
        organization_type=request.organization_type,
        organization_street_name=request.organization_street_name,
        country=request.country,
        city=request.city,
        postal_code=request.postal_code,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, id):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return user

def get_all_users(db: Session):
    sellers = db.query(models.User).all()
    return sellers

def update_user(db: Session, request: schemas.User, id):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    user.update(request.dict())
    db.commit()
    return 'done'

def delete_user(db: Session, id):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'
