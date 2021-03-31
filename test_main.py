import pytest

from sanic import Sanic
from sanic import Blueprint
from sanic.request import Request
from sanic.response import text
from sanic.exceptions import InvalidUsage

from sanic_testing import TestManager


@pytest.fixture
def app():
    app = Sanic(__name__)

    rest = Blueprint("rest", url_prefix="/rest")

    @rest.get("/users")
    async def select(request: Request, user: dict):
        pass

    @rest.put("/users")
    async def update(request: Request):
        if request.json is None:
            raise InvalidUsage("Missing json payload")
        else:
            return text("ok")

    app.blueprint(rest)

    return TestManager(app)


def test_json_payload(app):
    request, response = app.test_client.put("/rest/users", json={})
    assert response.status == 200
