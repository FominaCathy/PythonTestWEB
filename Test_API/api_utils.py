from zeep import Client, Settings
import yaml

with open('config.yaml') as fy:
    data = yaml.safe_load(fy)

settings = Settings(strict=False)
client = Client(wsdl=data['wdsl'], settings=settings)


def test_check(text):
    return client.service.checkText('малоко')[0]['s']


