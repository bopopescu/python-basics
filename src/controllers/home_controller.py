from src import app
from flask import Blueprint
from src.models.product import Product
from src.models.category import Category
from src.models import Base, session

blueprint = Blueprint("home", __name__)

@app.route('/')
def hello_world():
    product = Product(name="product_1")    
    category = Category(name="category_1", description='description')
    product.categories = [category]
    
    session.add(product)
    session.commit()

    return 'Hello, World!'

