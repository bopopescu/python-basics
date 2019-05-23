from src.models import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from src.models.categories_products import categories_products


class Product(Base):
	__tablename__ = "products"
	name = Column(String(50), nullable=False)
	categories = relationship(
        "Category",
        secondary=categories_products,
        back_populates="products")
	
	
	def __init__(self, name):
		self.name = name