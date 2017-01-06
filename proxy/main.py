from aiohttp import web
from .routes import setup_routes

def run_proxy(loop):
    app = web.Application(loop=loop)
    setup_routes(app)
    web.run_app(app, host='127.0.0.1', port=8080)
