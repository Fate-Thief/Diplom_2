import pytest

from api_client import ApiClient
from helpers import new_user_body


@pytest.fixture(scope="session")
def api():
    return ApiClient()


@pytest.fixture(scope="session")
def create_user(api):
    new_user = new_user_body()
    response = api.create_new_user(new_user)
    response_body = response.json()
    yield response, new_user
    api.delete_user(token=response_body["accessToken"])
