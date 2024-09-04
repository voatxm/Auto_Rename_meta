# plugins/web_support.py

from aiohttp import web

async def web_server():
    app = web.Application()
    # Add your routes and handlers here
    return app
