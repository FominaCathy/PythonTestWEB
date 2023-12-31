"""класс для работы с API"""
import logging
import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)


class BaseAPI:
    """класс для работы с API"""

    def __init__(self):
        try:
            self.session = requests.Session()
            self.token = self.session.post(url=testdata['url_auto'],
                                           data={'username': testdata['username'],
                                                 'password': testdata['password']}).json()['token']
            logging.debug(f'инициализация сессии и получение токена для {testdata["username"]}')
        except:
            logging.exception(f'нее удалось получить токен для {testdata["username"]} или открыть сессию requests')

    def get_post(self, owner=None):
        try:
            res = self.session.get(url=testdata['url_post'], headers={"X-Auth-Token": self.token},
                                   params={"owner": owner})
            logging.info(f'получены посты с параметрами: юзер: {testdata["username"]}, автор: {owner= }')
        except:
            logging.exception('нее удалось получить посты')
            return None
        return res.json()['data']

    def create_post(self, title, description, content):
        try:
            self.session.post(url=testdata['url_post'], headers={'X-Auth-Token': self.token},
                              params={"title": title, 'description': description, 'content': content})
            logging.info(f'создан пост на странице {testdata["username"]}')
        except:
            logging.exception(f'нее удалось создать пост на странице {testdata["username"]}')
