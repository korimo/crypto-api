# app/coingecko.py

import httpx

COINGECKO_API = "https://api.coingecko.com/api/v3"

async def get_coin_info_by_symbol(symbol: str):
    async with httpx.AsyncClient() as client:
        coins = (await client.get(f"{COINGECKO_API}/coins/list")).json()
        coin = next((c for c in coins if c["symbol"].lower() == symbol.lower()), None)
        if not coin:
            return None

        details = (await client.get(f"{COINGECKO_API}/coins/{coin['id']}?localization=false")).json()
        return {
            "symbol": coin["symbol"],
            "name": coin["name"],
            "coingecko_id": coin["id"],
            "current_price": details["market_data"]["current_price"]["usd"],
            "market_cap": details["market_data"]["market_cap"]["usd"]
        }
