from aiohttp import web
import asyncio, aiohttp

import sys

async def index(request):
    url = str(request.rel_url)
    response = await method(url)
    return web.Response(text="text")



async def fetch(session, url):
    with aiohttp.Timeout(10):
        response = await session.get(url)
        try:
            return (await response.text())
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
