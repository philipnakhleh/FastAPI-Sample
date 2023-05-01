from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
import hashlib



def get_all(db: Session):
    sellers = db.query(models.Seller).all()
    return {
        'data' : sellers
    }

def create(db: Session, request: schemas.Seller, code: bytes):
    new_seller = models.Seller(
        first_name=request.first_name,
        last_name=request.last_name,
        birthday=request.birthday,
        email=request.email,
        phone=request.phone,
        organization_website=request.organization_website,
        organization_name=request.organization_name,
        organization_type=request.organization_type,
        country=request.country,
        city=request.city,
        postal_code=request.postal_code,
        need_fund = request.need_fund,
        funding_amount = request.funding_amount,
        offer = request.offer,
        Description = request.Description,
        verification_code = code,
        pain_points = request.pain_points,
        country_code= request.country_code
    )

    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return {
        'id' : new_seller.id
    }


def delete(db: Session, id):
    seller = db.query(models.Seller).filter(models.Seller.id == id)
    if not seller.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    seller.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_seller(db: Session, request: schemas.Seller, id):
    seller = db.query(models.Seller).filter(models.Seller.id == id)
    if not seller.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    seller.update(request.dict())
    db.commit()
    return 'done'


def get_id(db: Session, id):
    seller = db.query(models.Seller).filter(models.Seller.id == id).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return seller

def verify_code(db: Session, id, code):
    seller = db.query(models.Seller).filter(models.Seller.id == id).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    if(code == seller.verification_code):
        seller.verified = True
        db.commit()
        return {
            'message' : 'verified'
        }
    return {
        'message': 'Wrong Code'
    }