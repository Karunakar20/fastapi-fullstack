from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100)) 
    description = Column(String(100))
    quantity = Column(Integer)   
    price = Column(Integer)      

    __tablename__ = "products" 
    
  