from aiohttp import web
import asyncio
import aiohttp
import redis
import sys


async def index(request):
    url = str(request.rel_url)
    result = view_cache(url)
    return web.Response(text=result)


async def fetch(session, url):
    with aiohttp.Timeout(10):
        response = await session.get(url)
        try:
            return await response.text()
        finally:
            if sys.exc_info()[0] is not None:
                response.close()
            else:
                await response.release()


async def method(url):
    loop = asyncio.get_event_loop()
    with aiohttp.ClientSession(loop=loop) as session:
        html = loop.run_until_complete(
            fetch(session, 'http://localhost:8888/student'))
        print(html)
        return "response"

    
async def view_cache(url):
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
    if redis_db.get('url') is None:
        # realizeaza cerere la nod
        result = await method(url)
        redis_db.setex('url', 60000, result)
    else:
        result = redis_db.get('url')
        return result
