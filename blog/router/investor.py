from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from typing import List
from ..database import get_db
from ..repository import investor
import math, random
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
import hashlib

conf = ConnectionConfig(
    MAIL_USERNAME = "cozmosluna",
    MAIL_PASSWORD = "owleenokwwbhhbwy",
    MAIL_FROM = "cozmosluna@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Cozmos Luna Mission",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


def generate_verification_code():
    digits = "0123456789"
    code = ""

    for i in range(6):
        code += digits[math.floor(random.random() * 10)]

    return code



router = APIRouter(
    prefix= '/investor',
    tags= ['investor']
)


@router.get('/')
def all(db: Session = Depends(get_db)):
    return investor.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Investor, db: Session = Depends(get_db)):
    code = generate_verification_code()
    emails = [request.email]
    template = f'''
        Hi {request.first_name}, I am Cozmos, Your Verification code is:
        {code}

        Thank you.
        '''
    message = MessageSchema(
        subject="Verification Code",
        recipients=emails,
        body=template,
        subtype="plain"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    hashed = hashlib.sha256(code.encode()).hexdigest()

    return investor.create(db, request, hashed)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id, db: Session = Depends(get_db)):
    return investor.delete(db, id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_buyer(id, request: schemas.Investor, db: Session = Depends(get_db)):
    return investor.update(db, request, id)

@router.get('/{id}', status_code=200)
def show(id, db: Session = Depends(get_db)):
    return investor.get_id(db, id)

@router.post('/verify/{id}', status_code=200)
def verify(id, code: str, db: Session = Depends(get_db)):
    hashed = hashlib.sha256(code.encode()).hexdigest()
    return investor.verify_code(db, id, hashed)

