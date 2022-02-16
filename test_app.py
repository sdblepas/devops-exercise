import pytest
import app
import json
from flask import session
@pytest.fixture
def application():
    application = app.app
    application.config.update({
        "TESTING" : True,
        "WTF_CSRF_ENABLED" : False,
        "SECRET_KEY" : "TESTINGKEY"
        })
    yield application

@pytest.fixture
def client(application):
    return application.test_client()

def test_signup(client):
    with client:
        response = client.post("/signup", data ={
            "username": "Test",
            "password":"test",
            "email" : "test@test.com"
            })
        assert response.status_code == 200 , response.data
def test_login(client):
    with client:
        response = client.post("/", data ={
            "username": "Test",
            "password":"test",
            "email" : "test@test.com"
            })
        assert response.status_code == 200, response.data
