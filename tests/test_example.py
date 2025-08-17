# tests/test_example.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("APP_URL")

def test_sum():
    assert 1 + 1 == 2

def test_upper():
    assert "abc".upper() == "ABC"

def test_api():
    req = requests.get(f"{URL}/objects")
    assert req.status_code == 200