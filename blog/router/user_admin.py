from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import fastapi.security as _security
from .. import schemas, models
import jwt
from ..database import get_db
import passlib.hash as _hash
from ..repository import buyer, seller, investor


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
    if not login.verify_password(form_data.password):
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

# @router.post('/create_user')
# def add_user(
#     db: Session = Depends(get_db),
# ):
#     new_user = models.User(
#         username='admin@cozmos-space.com',
#         password=_hash.bcrypt.hash('cozmos-space@1234567890')
#     )
#
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)