import httpx
import json
from redis_client import redis_client

COINGECKO_API = "https://api.coingecko.com/api/v3"

async def get_crypto_from_coingecko(symbol: str):
    cache_key = f"cg:{symbol.lower()}"
    cached = await redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    async with httpx.AsyncClient() as client:
        coins = (await client.get(f"{COINGECKO_API}/coins/list")).json()
        coin = next((c for c in coins if c["symbol"].lower() == symbol.lower()), None)
        if not coin:
            return None

        details = (await client.get(f"{COINGECKO_API}/coins/{coin['id']}?localization=false")).json()
        data = {
            "symbol": coin["symbol"],
            "name": coin["name"],
            "coingecko_id": coin["id"],
            "current_price": details["market_data"]["current_price"]["usd"],
            "market_cap": details["market_data"]["market_cap"]["usd"]
        }
        await redis_client.set(cache_key, json.dumps(data), ex=3600)
        return data

