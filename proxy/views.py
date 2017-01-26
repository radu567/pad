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
    loop = asyncio.get_event_loop()
    result = await view_cache(url)
    return web.Response(text=result)

def create_url(url):
    # cream linkul
    host = 'http://localhost:'
    port = q.get()
    q.put(port)
    print("port ", port)
    return host + str(port) + url

async def fetch(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()

async def main(loop, url):
    async with aiohttp.ClientSession(loop=loop) as client:
        html = await fetch(client, create_url(url))
        print(html)
        return html

async def view_cache(url):
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
    if redis_db.get('url') is None:
        # realizeaza cerere la nod
        print("From database")
        loop = asyncio.get_event_loop()
        try:
            result = await main(loop, url)
        except:
            result = "Cannot receive data from sever"
        redis_db.setex('url', 30, result)
    else:
        print("From cache")
        result = redis_db.get('url')
        result = str(result.decode())
    return result
