from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.router import seller, user, buyer, investor, email

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(seller.router)

app.include_router(buyer.router)

app.include_router(investor.router)

# app.include_router(email.router)

#app.include_router(authentication.router)



