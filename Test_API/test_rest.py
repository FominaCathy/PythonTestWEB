import requests
import yaml

with open('config.yaml') as fy:
    data = yaml.safe_load(fy)

s = requests.Session()


def test_one(get_token, ost_title):
    res = s.get(url=data['url_post'], headers={"X-Auth-Token": get_token}, params={"owner": "notMe"}).json()['data']
    res_title = [i['title'] for i in res]

    assert ost_title in res_title, 'FAIL'


def test_create_new_post(get_token):
    res = s.post(url=data['url_post'], headers={'X-Auth-Token': get_token},
                 params={"title": data['title_post'],
                         'description': data["description_post"],
                         'content': data['content_post']})

    res = s.get(url=data['url_post'], headers={"X-Auth-Token": get_token}).json()['data']
    res_title = [i['title'] for i in res]
    assert data['title_post'] in res_title, 'FAIL'
