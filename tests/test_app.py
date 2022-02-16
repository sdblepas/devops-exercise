import pytest
import app
import json
@pytest.fixture
def app():
    client = app.app.test_client
    yield client

def test_signup(client):
    response = client.post("/signup", data ={
        "name": Test
        "password":test
        })
    assert response.status_code == 200
def test_login():
    return True
