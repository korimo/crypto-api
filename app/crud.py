    # app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import update

def get_crypto_by_symbol(db: Session, symbol: str):
    return db.query(models.Cryptocurrency).filter(models.Cryptocurrency.symbol == symbol).first()

def get_all_cryptos(db: Session):
    return db.query(models.Cryptocurrency).all()

def create_crypto(db: Session, crypto_data: dict):
    db_crypto = models.Cryptocurrency(**crypto_data)
    db.add(db_crypto)
    db.commit()
    db.refresh(db_crypto)
    return db_crypto

def update_crypto(db: Session, crypto_data: dict):
    crypto = get_crypto_by_symbol(db, symbol)
    Cryptomo = models.Cryptocurrency
    if crypto:
        stmt = (
                update(Cryptomo)
                .where(Cryptomo.symbol ==  symbol)
                .values(
                    name = crypto.name,
                    coingecko_id = crypto.coingecko_id,
                    current_price = crypto.current_price,
                    market_cap = crypto.market_cap
                )
            )
    db.execute(db_crypto)
    db.commit()
    db.refresh(db_crypto)
    return db_crypto

def delete_crypto(db: Session, symbol: str):
    crypto = get_crypto_by_symbol(db, symbol)
    if crypto:
        db.delete(crypto)
        db.commit()
    return crypto
