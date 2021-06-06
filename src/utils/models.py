import os
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property, relationship
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.util.langhelpers import hybridproperty

Base = declarative_base()


DATABASE_CONNECTION_STRING = '{drivername}://{user}:{password}@{host}:{port}/{db_name}'.format(
    drivername='postgresql',
    user=os.environ.get('PG_USERNAME', 'postgres'),
    password=os.environ.get('PG_PASSWORD'),
    host=os.environ.get('PG_HOST', 'localhost'),
    port=os.environ.get('PG_PORT', '5432'),
    db_name=os.environ.get('PG_DATABASE', 'burplist'),
)


def db_connect():
    """
    Performs database connection using database settings from settings.py
    Returns sqlalchemy engine instance
    """
    return create_engine(DATABASE_CONNECTION_STRING)


def create_table(engine):
    """
    Creates database table
    """
    Base.metadata.create_all(engine)


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False, index=True)
    product = relationship('Product', backref='prices', cascade='delete')

    price = Column('price', Float)
    updated_on = Column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'Price(price={self.price}, product={self.product.name})'


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = (UniqueConstraint('quantity', 'url'),)

    id = Column(Integer, primary_key=True)
    platform = Column(String(), nullable=False)

    name = Column(String(), index=True, nullable=False)
    url = Column(String(), nullable=False)

    brand = Column(String(), nullable=True, default=None)
    style = Column(String(), nullable=True, default=None)
    origin = Column(String(), nullable=True, default=None)

    abv = Column(Float(), nullable=True, default=None)
    volume = Column(Integer(), nullable=True, default=None)
    quantity = Column(Integer(), nullable=False)

    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    last_price = column_property(
        select([Price.price]).
        where(Price.product_id == id).
        order_by(Price.id.desc()).
        limit(1).  # NOTE: We have to always limit this as 1 to prevent `CardinalityViolation: more than one row returned by a subquery used as an expression`
        as_scalar()
    )

    @hybridproperty
    def price_per_quantity(self) -> float:
        return self.last_price / self.quantity

    def __repr__(self) -> str:
        return f'Product({self.name}, vendor={self.vendor})'
