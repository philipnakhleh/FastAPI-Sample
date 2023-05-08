import datetime

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import fastapi.security as _security
from .. import schemas, models
import jwt
from ..database import get_db
import passlib.hash as _hash
from ..repository import buyer, seller, investor
import math
import random
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig


router = APIRouter(
    prefix= '/user',
    tags= ['admin']
)

JWT_SECRET = 'secter'
oauth2schema = _security.OAuth2PasswordBearer(tokenUrl= '/user/login')

async def get_current_user(
         db: Session = Depends(get_db),
        token: str = Depends(oauth2schema)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        name = payload['username']
        user = db.query(models.User).filter(models.User.username == name).first()
        return schemas.User.from_orm(user)
    except:
        raise HTTPException(status_code=401, detail="Invalid Email Or password")

@router.post('/login')
async def generate_token(form_data: _security.OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    login = db.query(models.User).filter(models.User.username == form_data.username).first()

    if not login or not login.verify_password(form_data.password):
        raise HTTPException(status_code=401, detail="Invalid Email Or password")

    user = db.query(models.User).filter(models.User.username == form_data.username).first()

    schemas.User.from_orm(user)
    dic = {
        'username': user.username,
        'pass': user.password
    }
    token = jwt.encode(dic, JWT_SECRET)

    return dict(access_token=token, token_type='bearer')


@router.get('/stats')
def get_stats(
        db: Session = Depends(get_db),
        user: schemas.User = Depends(get_current_user)
):
    sellers = db.query(models.Seller).all()
    buyers = db.query(models.Buyer).all()
    verified_sellers = db.query(models.Seller).filter(models.Seller.verified).all()
    verified_buyers = db.query(models.Buyer).filter(models.Buyer.verified).all()
    subscribers = db.query(models.Subscribers).all()
    messages = db.query(models.Messages).all()

    return {
        'total number' : len(sellers) + len(buyers),
        'total verified' : len(verified_buyers) + len(verified_sellers),
        'sellers number' : len(sellers),
        'buyers number' : len(buyers),
        'verified sellers number' : len(verified_sellers),
        'verified buyers number' : len(verified_buyers),
        'total subscribers' : len(subscribers),
        'total messages' : len(messages)
    }

@router.get('/get_buyers')
def all(db: Session = Depends(get_db),
        user: schemas.User = Depends(get_current_user)):
    return buyer.get_all(db)

@router.get('/get_sellers')
def all(db: Session = Depends(get_db),
        user: schemas.User = Depends(get_current_user)):
    return seller.get_all(db)

def generate_verification_code():
    digits = "0123456789"
    code = ""

    for i in range(6):
        code += digits[math.floor(random.random() * 10)]

    return code

@router.post('/forgot')
async def forgot_password(
        username: str,
        db: Session = Depends(get_db)
    ):
    conf = ConnectionConfig(
        MAIL_USERNAME="no-reply@cozmos-space.com",
        MAIL_PASSWORD="Ov1fIA4T#R)F",
        MAIL_FROM="no-reply@cozmos-space.com",
        MAIL_PORT=465,
        MAIL_SERVER="mail.cozmos-space.com",
        MAIL_FROM_NAME="no-reply",
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=True,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True
    )
    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    code = generate_verification_code()
    emails = [username]
    template = f'You Password reset code is {code}'
    message = MessageSchema(
        subject="Password Reset",
        recipients=emails,
        body=template,
        subtype="plain"
    )

    fm = FastMail(conf)
    try:
        await fm.send_message(message)
    except:
        raise HTTPException(status_code=404, detail="Error in sending email")

    forgot_password_new = models.reset_password(
        username= username,
        verification_code= code,
        time_stamp=datetime.datetime.now(),
        verified = False
    )
    db.add(forgot_password_new)
    db.commit()
    db.refresh(forgot_password_new)

    return {
        'data': 'Done'
    }


@router.put('/verify_code')
def send_code(
        req: schemas.enter_code
        ,db: Session = Depends(get_db)
    ):
    name = req.username
    code = req.verification_code

    users = db.query(models.reset_password).filter(models.reset_password.username == name).order_by(models.reset_password.id.desc()).first()

    if (datetime.datetime.now() - users.time_stamp).total_seconds() / 60.0 > 30.0:
        raise HTTPException(status_code=403, detail="code expired")

    if users.verified:
        raise HTTPException(status_code=403, detail="code expired")

    if code == users.verification_code:
        users.verified = True
        db.commit()

        dic = {
            'username': name,
            'time': str(datetime.datetime.now())
        }
        token = jwt.encode(dic, JWT_SECRET)

        return dict(access_token=token, token_type='bearer')


    raise HTTPException(status_code=403, detail="worng code")

@router.put('/update_password')
def update_pass(
        token: str,
        new_pass: str,
        db: Session = Depends(get_db)
    ):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        name = payload['username']
        date = payload['time']
        time_stamp = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        if (datetime.datetime.now() - time_stamp).total_seconds() / 60.0 > 30.0:
            raise HTTPException(status_code=403, detail="Request expired")

        user = db.query(models.User).filter(models.User.username == name).first()

        user.password = _hash.bcrypt.hash(new_pass)
        db.commit()

        return {
               'data' : 'done'
        }

    except Exception as e:
        raise e
# @router.post('/create_user')
# def add_user(
#     db: Session = Depends(get_db),
# ):
#     new_user = models.User(
#         username='philipnakhleh@gmail.com',
#         password=_hash.bcrypt.hash('cozmos-space@1234567890')
#     )
#
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)