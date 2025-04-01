# app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, coingecko

import uvicorn

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Crypto API is running!"}

@app.post("/cryptos/", response_model=schemas.Cryptocurrency)
async def add_crypto(symbol_data: schemas.CryptocurrencyCreate, db: Session = Depends(get_db)):
    db_crypto = crud.get_crypto_by_symbol(db, symbol_data.symbol)
    if db_crypto:
        raise HTTPException(status_code=400, detail="Cryptocurrency already exists.")

    coin_info = await coingecko.get_coin_info_by_symbol(symbol_data.symbol)
    if not coin_info:
        raise HTTPException(status_code=404, detail="Cryptocurrency symbol not found on Coingecko.")

    return crud.create_crypto(db, coin_info)

@app.get("/cryptos/", response_model=list[schemas.Cryptocurrency])
def get_all_cryptos(db: Session = Depends(get_db)):
    return crud.get_all_cryptos(db)

@app.get("/cryptos/{symbol}", response_model=schemas.Cryptocurrency)
def get_crypto(symbol: str, db: Session = Depends(get_db)):
    crypto = crud.get_crypto_by_symbol(db, symbol)
    if not crypto:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found.")
    return crypto

@app.delete("/cryptos/{symbol}")
def delete_crypto(symbol: str, db: Session = Depends(get_db)):
    deleted = crud.delete_crypto(db, symbol)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found.")
    return {"message": "Deleted"}

# Optional: run if called directly
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
