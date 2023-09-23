import pytest
import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as fy:
    data = yaml.safe_load(fy)


@pytest.fixture()
def get_token():
    result = S.post(url=data['url_auto'], data={'username': data['username'], 'password': data['password']})
    return result.json()['token']


@pytest.fixture()
def ost_title():
    return 'Пхукет'


@pytest.fixture()
def coord_one():
    return '37.7891838', '-122.4033522'


@pytest.fixture()
def search_object():
    return 'One Montgomery Tower'


@pytest.fixture()
def valid_text():
    return 'молоко'


@pytest.fixture()
def invalid_text():
    return 'малоко'
