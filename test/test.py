import os
import requests
#import pytest

BASE_URL = os.environ.get("APP_BASE_URL", "http://app:8000")



def test_simple():
    assert True



def test_healthcheck():
    url = f"{BASE_URL}/"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_read_item():
    item_id = 42
    q = "example"
    url = f"{BASE_URL}/items/{item_id}"
    params = {"q": q}
    response = requests.get(url, params=params)
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": q}
