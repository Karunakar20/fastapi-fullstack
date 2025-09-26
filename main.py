# from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Depends
from db_config import engine,db_connection
import models
from sqlalchemy.orm import Session
from service import ProductService
from utilities.common import ProductSchema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # allow frontend,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {"Hello": "Hai"}

@app.post("/products")
def create_product( request: ProductSchema,db: Session = Depends(db_connection)):
    product = ProductService(db).add_or_update_product(request)
    return product

@app.get("/products")
def get_products(db: Session = Depends(db_connection)):
    return ProductService(db).get_products()

@app.get("/product",)
def get_products(id: int,db: Session = Depends(db_connection)):
    return ProductService(db).get_product(id)

@app.delete('/product')
def delete_products(id: int,db: Session = Depends(db_connection)):
    return ProductService(db).delete(id)


    