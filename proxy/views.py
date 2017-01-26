from aiohttp import web
import asyncio
import aiohttp
import redis
import sys
import queue

q = queue.Queue()
ports=[7777, 8888, 9999]
for i in ports:
    q.put(i)

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


def create_url(url):
    # cream linkul
    url = url
    host = 'http://localhost:'
    port = q.get()
    q.put(port)
    return host + str(port) + url


async def method(url):
    loop = asyncio.get_event_loop()
    with aiohttp.ClientSession(loop=loop) as session:
        html = loop.run_until_complete(
            fetch(session, create_url(url)))
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
