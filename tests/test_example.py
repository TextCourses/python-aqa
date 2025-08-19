# tests/test_example.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("APP_URL")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

def test_sum():
    assert 1 + 1 == 2

def test_upper():
    assert "abc".upper() == "ABC"

def test_api():
    req = requests.get(f"{URL}/objects")
    assert req.status_code == 200

def test_api_auth():
    headers = {
        "Accept": "application/json",
        "Authorization": AUTH_TOKEN
    }
    response = requests.get("https://httpbin.org/bearer", headers=headers)
    assert response.status_code == 200