import pytest


@pytest.fixture
def app():
    from eagle_python_project import create_app

    return create_app()


def test_index_returns_200(app):
    request, response = app.test_client.get("/")
    assert response.status == 200


def test_index_put_not_allowed(app):
    request, response = app.test_client.put("/")
    assert response.status == 405
