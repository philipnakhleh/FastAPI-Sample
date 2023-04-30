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

    subscriber = db.query(models.Subscribers).filter(models.Subscribers.email == request.email)
    if subscriber.first():
        raise HTTPException(status_code=status.HTTP_302_FOUND,
                            detail=f'Subscriber Exists')

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
    return get_blogs()

@router.get('/get_blogs_by_page')
def get_blogs_for_page(pagenum: int, length: int):
    blogs =  get_blogs()['data']
    all = len(blogs)

    number = int(all // length)
    if all % length != 0:
        number+=1

    if pagenum >= number or pagenum < 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Limit of pages exceeded')

    r = all
    if pagenum*length+length < r:
        r = pagenum*length+length

    ret_blogs = blogs[pagenum*length: r]

    return {
        'blogs' : ret_blogs,
        'length': number
    }

@router.delete('/delete_sub', status_code=status.HTTP_202_ACCEPTED)
def destroy(email: str, db: Session = Depends(get_db)):
    subscriber = db.query(models.Subscribers).filter(models.Subscribers.email == email)
    if not subscriber.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Subscriber is not found')
    subscriber.delete(synchronize_session=False)
    db.commit()
    return {
        'message' : 'done'
    }

@router.get('/settings')
def all():
    return {
        'Language' : 'ar',
        'Organization type' : [
            {'name':'Company',
             'mandatory': True},
            {'name' : 'University',
             'mandatory' : True},
            {'name':'Other',
             'mandatory' : False},
        ]
    }