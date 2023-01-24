from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas

def get_all(db: Session):
    investors = db.query(models.Investor).all()
    return investors
def get_all(db: Session):
    investors = db.query(models.Investor).all()
    return investors

def create(db: Session, request: schemas.Investor, code):
    new_investor = models.Investor(
        first_name=request.first_name,
        last_name=request.last_name,
        birthday=request.birthday,
        email=request.email,
        phone=request.phone,
        organization_name=request.organization_name,
        organization_type=request.organization_type,
        organization_website=request.organization_website,
        organization_street_name=request.organization_street_name,
        country=request.country,
        city=request.city,
        postal_code=request.postal_code,
        amount = request.amount,
        communication_time = request.communication_time,
        communication_type = request.communication_type,
        description = request.description,
        verification_code=code
    )
    db.add(new_investor)
    db.commit()
    db.refresh(new_investor)
    return {
        'id' : new_investor.id
    }


def delete(db: Session, id):
    investor = db.query(models.Investor).filter(models.Investor.id == id)
    if not investor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    investor.delete(synchronize_session=False)
    db.commit()
    return {
        'message': 'done'
    }


def update(db: Session, request: schemas.Investor, id):
    investor = db.query(models.Investor).filter(models.Investor.id == id)
    if not investor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    investor.update(request.dict())
    db.commit()
    return 'done'


def get_id(db: Session, id):
    investor = db.query(models.Investor).filter(models.Investor.id == id).first()
    if not investor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    return investor

def verify_code(db: Session, id, code):
    investor = db.query(models.Investor).filter(models.Investor.id == id).first()
    if not investor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
    if(code == investor.verification_code):
        investor.verified = True
        db.commit()
        return {
            'message' : 'verified'
        }
    return {
        'message': 'Wrong Code'
    }