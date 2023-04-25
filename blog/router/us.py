from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from typing import List
from ..database import get_db
from ..repository import blogs
import math, random
from ..blog_fetcher import get_blogs



router = APIRouter(
    prefix= '/us',
    tags= ['unidentified']
)


@router.get('/get_subscribers')
def all(db: Session = Depends(get_db)):
    ret = db.query(models.Subscribers).all()
    return ret

@router.post('/subscribe', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Subscribers, db: Session = Depends(get_db)):
    new_subscriber = models.Subscribers(
        email = request.email
    )

    db.add(new_subscriber)
    db.commit()
    db.refresh(new_subscriber)
    #TODO Send email for Subscription
    return {
        'message': 'Subscriber added'
    }

@router.post('/send_message', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Messages, db: Session = Depends(get_db)):
    new_message = models.Messages(
        email=request.email,
        content = request.content
    )

    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    #TODO send email for reciption
    return {
        'message': 'message added'
    }

@router.get('/get_messages')
def all(db: Session = Depends(get_db)):
    ret = db.query(models.Messages).all()
    return ret

@router.get('/get_blogs')
def medium_blogs():
    get_blogs()