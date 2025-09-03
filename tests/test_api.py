import pytest
import requests

@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com/posts/1"

@pytest.fixture
def payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

def test_create_post(api_url, payload):
    response = requests.post(api_url, json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]
    assert response.json()["userId"] == payload["userId"]