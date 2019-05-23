from src.models import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from src.models.categories_products import categories_products

class Category(Base):
    __tablename__ = "categories"
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    products = relationship(
        "Product",
        secondary=categories_products,
        back_populates="categories")
