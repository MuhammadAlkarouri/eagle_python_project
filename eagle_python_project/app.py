from uuid import uuid4

from sanic import Sanic
from sanic.response import json


async def lorem(request):
    return json({"hello": "world", "id": str(uuid4())})


def create_app():
    app = Sanic()
    app.add_route(lorem, "/")
    return app
