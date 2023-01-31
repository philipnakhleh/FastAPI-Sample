from fastapi import FastAPI
from blog import models, blogs_models
from blog.database import engine
from blog.router import seller, user, buyer, investor, email, blogs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)
blogs_models.Base.metadata.create_all(engine)

#Seller Route
app.include_router(seller.router)

#Blog Route
app.include_router(blogs.router)

#Buyer Route
app.include_router(buyer.router)

#Investor Route
app.include_router(investor.router)

#app.include_router(authentication.router)



