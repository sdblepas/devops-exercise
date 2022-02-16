import pytest
import requests

def test_health():
    requests.get("http://localhost:5000")
    assert request.status_code == 200
