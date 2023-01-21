from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas
from fastapi_mail import FastMail, MessageSchema
from pydantic import EmailStr
from typing import List


def create(db: Session, request: schemas.Buyer, code: str):
    new_buyer = models.Buyer(
        first_name= request.first_name,
        last_name= request.last_name,
        birthday= request.birthday,
        email= request.email,
        phone= request.phone,
        organization_name= request.organization_name,
        organization_website=request.organization_website,
        organization_type= request.organization_type,
        organization_street_name= request.organization_street_name,
        country= request.country,
        city= request.city,
        postal_code= request.postal_code,
        order = request.order,
        reason = request.reason,
        verification_code=code
    )

    db.add(new_buyer)
    db.commit()
    db.refresh(new_buyer)
    return {
        'id' : new_buyer.id
    }


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

def verify_code(db: Session, id, code):
    buyer = db.query(models.Buyer).filter(models.Buyer.id == id).first()
    if not buyer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    if(code == buyer.verification_code):
        buyer.verified = True
        db.commit()
        return {
            'message' : 'verified'
        }
    return {
        'message': 'Wrong Code'
    }