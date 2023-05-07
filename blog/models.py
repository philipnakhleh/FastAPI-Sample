from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, LargeBinary
import passlib.hash as _hash


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
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)
    need_fund = Column(Boolean)
    funding_amount = Column(Integer)
    offer = Column(String)
    Description = Column(String)
    pain_points = Column(String)
    country_code = Column(String)
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
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)
    order = Column(String)
    reason = Column(String)
    pain_points = Column(String)
    country_code = Column(String)
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
    country = Column(String)
    city = Column(String)
    postal_code = Column(String)
    amount = Column(Integer)
    communication_time = Column(String)
    communication_type = Column(String)
    description = Column(String)
    pain_points = Column(String)
    country_code = Column(String)
    verification_code = Column(String, default="")
    verified = Column(Boolean, default=False)

class Subscribers(Base):
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)

class Messages(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    content = Column(String)
    send_date = Column(Date)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.password)