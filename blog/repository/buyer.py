from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

def get_all(db: Session):
    buyers = db.query(models.Buyer).all()
    return buyers

def create(db: Session, request: schemas.Buyer):
    new_buyer = models.Buyer(
        first_name= request.first_name,
        last_name= request.last_name,
        birthday= request.birthday,
        email= request.email,
        phone= request.phone,
        organization_name= request.organization_name,
        organization_type= request.organization_type,
        organization_street_name= request.organization_street_name,
        country= request.country,
        city= request.city,
        postal_code= request.postal_code,
        order = request.order,
        reason = request.reason,
    )
    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return new_buyer


def delete(db: Session, id):
    buyer = db.query(models.Buyer).filter(models.Buyer.id == id)
    if not buyer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    buyer.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_buyer(db: Session, request: schemas.Buyer, id):
    buyer = db.query(models.Buyer).filter(models.Buyer.id == id)
    if not buyer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    buyer.update(request.dict())
    db.commit()
    return 'done'


def get_id(db: Session, id):
    buyer = db.query(models.Buyer).filter(models.Buyer.id == id).first()
    if not buyer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return buyer
