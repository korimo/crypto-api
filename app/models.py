# app/models.py

from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Cryptocurrency(Base):
    __tablename__ = "cryptocurrencies"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    coingecko_id = Column(String, nullable=False)
    current_price = Column(Float, nullable=True)
    market_cap = Column(Float, nullable=True)
