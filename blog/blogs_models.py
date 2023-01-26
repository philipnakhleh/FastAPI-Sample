from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, LargeBinary

class Blog(Base):
    __tablename__ = 'blogs_info'
    id = Column(Integer, primary_key=True, index=True)
    blog_title = Column(String)
    blog_description = Column(String)
    blog_date = Column(Date)
    blog_summarization = Column(String)
    blog_writer = Column(String)
    blog_reviewer = Column(String, nullable = True)
