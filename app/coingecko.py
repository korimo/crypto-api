import httpx
import json
from redis_client import redis_client

async def get_crypto_from_coingecko(symbol: str):
    cache_key = f"cg:{symbol.lower()}"
    cached = await redis_client.get(cache_key)
    if cached:
        return json.loads(cached)

    url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            await redis_client.set(cache_key, json.dumps(data), ex=3600)
            return data
        return None
