from model import Base, Product

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(price,quantity,description,OnSale):
	Product_object=Product(
		price=price,
		quantity=quantity,
		description=description,
		OnSale=OnSale)
	session.add(Product_object)
	session.commit()




def update_product(id,price,OnSale):
	Product_object=session.query(
	Product).filter_by(
	id=id).first()
	Product_object.price=price
	Product_object.OnSale=OnSale
	session.commit()




def delete_product(id):
	session.query(Product).filter_by(id=id).delete()
	session.commit()

def get_product(id):
  pass
