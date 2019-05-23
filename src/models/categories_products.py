from sqlalchemy import Table, String, Column, ForeignKey
from src.models import Base

categories_products = Table('categories_products', Base.metadata,
    Column('category_id', String(36), ForeignKey('categories.id')),
    Column('product_id', String(36), ForeignKey('products.id'))
)