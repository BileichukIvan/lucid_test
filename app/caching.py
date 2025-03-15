import time
from functools import lru_cache
from app.config import CACHE_EXPIRY

_cache = {}


def cache_get(key):
    """Retrieve cached data if valid."""
    entry = _cache.get(key)
    if entry and time.time() - entry["timestamp"] < CACHE_EXPIRY:
        return entry["data"]
    return None


def cache_set(key, data):
    """Store data in cache with a timestamp."""
    _cache[key] = {"data": data, "timestamp": time.time()}