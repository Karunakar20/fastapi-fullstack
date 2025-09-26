from sqlalchemy.orm import Session
import models  # your database models
from utilities.common import ProductSchema


class ProductService:
     def __init__(self, db: Session):
          self.db = db

     def add_or_update_product(self,data: ProductSchema):
          
          if data.id:  
               product = self.db.query(models.Products).filter(models.Products.id == data.id).first()
               if product:
                    # Update existing
                    product.name = data.name
                    product.description = data.description
                    product.quantity = data.quantity
                    product.price = data.price
          else:
               product = models.Products(
                    name=data.name,
                    description=data.description,
                    quantity=data.quantity,
                    price=data.price
               )
               self.db.add(product)
               
          self.db.commit()
          self.db.refresh(product)

          return {"responce": product.id}
     
     def get_products(self):
          products = self.db.query(models.Products).all()
          return products
     
     def get_product(self,id):
          product = self.db.query(models.Products).filter(models.Products.id == id).first()
          return ProductSchema.model_validate(product)
     
     def delete(self,id):
          product = self.db.query(models.Products).filter(models.Products.id == id).first()
          self.db.delete(product)
          self.db.commit()
          
