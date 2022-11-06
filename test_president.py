import unittest
import requests

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]


def test_ddg1():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    assert "Presidents of the United States" in rsp_data["Heading"]



