import pytest
import requests

url_ddg = "https://api.duckduckgo.com"


@pytest.fixture
def pres_resp():
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    return rsp_data


@pytest.fixture
def pres_list():
    presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Buren", "Harrison", "Tyler",
                  "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
                  "Garfield", "Arthur", "Cleveland", "Harrison", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
                  "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter",
                  "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]

    return presidents


def test_ddg2(pres_resp, pres_list):
    topics = pres_resp["RelatedTopics"]
    resulttext = ""
    for topic in topics:
        resulttext += topic["Text"]

    for president in pres_list:
        assert president in resulttext
