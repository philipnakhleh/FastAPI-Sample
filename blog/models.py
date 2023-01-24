from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, LargeBinary
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users_info'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    email = Column(String)
    phone = Column(String)
    organization_name = Column(String)
    organization_type = Column(String)
    organization_street_name = Column(String)
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)




class Seller(Base):
    __tablename__ = 'sellers_info'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    email = Column(String)
    phone = Column(String)
    organization_name = Column(String)
    organization_type = Column(String)
    organization_website = Column(String)
    organization_street_name = Column(String)
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)
    need_fund = Column(Boolean)
    funding_amount = Column(Integer)
    offer = Column(String)
    Description = Column(String)
    verification_code = Column(String, default="")
    verified = Column(Boolean, default=False)


class Buyer(Base):
    __tablename__ = 'buyers_info'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    email = Column(String)
    phone = Column(String)
    organization_name = Column(String)
    organization_type = Column(String)
    organization_website = Column(String)
    organization_street_name = Column(String)
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)
    order = Column(String)
    reason = Column(String)
    verification_code = Column(String, default="")
    verified = Column(Boolean, default=False)



class Investor(Base):
    __tablename__ = 'investors_info'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(Date)
    email = Column(String)
    phone = Column(String)
    organization_name = Column(String)
    organization_type = Column(String)
    organization_website = Column(String)
    organization_street_name = Column(String)
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)
    amount = Column(Integer)
    communication_time = Column(String)
    communication_type = Column(String)
    description = Column(String)
    verification_code = Column(String, default="")
    verified = Column(Boolean, default=False)