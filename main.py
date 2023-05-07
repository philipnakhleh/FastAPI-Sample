from fastapi import FastAPI
from blog import models, blogs_models
from blog.database import engine
from blog.router import seller, buyer, investor, us, blogs, Settings, user_admin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

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

#Subscribers_router
app.include_router(us.router)

#Settings Route
app.include_router(Settings.router)
#app.include_router(authentication.router)

app.include_router(user_admin.router)




