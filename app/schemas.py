# app/schemas.py

from pydantic import BaseModel
from typing import Optional

class CryptocurrencyBase(BaseModel):
    symbol: str

class CryptocurrencyCreate(CryptocurrencyBase):
    pass

class Cryptocurrency(CryptocurrencyBase):
    id: int
    name: str
    coingecko_id: str
    current_price: Optional[float]
    market_cap: Optional[float]

    class Config:
        orm_mode = True
