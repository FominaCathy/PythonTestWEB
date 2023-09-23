import requests

S = requests.Session()


def get_sites(lat, long, radius, limit=100):
    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f'{limit}',
        "gsradius": f'{radius}',
        "action": "query"
    }

    r = S.get(url=URL, params=PARAMS)
    pages = r.json()['query']['geosearch']
    sites = [i["title"] for i in pages]

    return sites


def test_tower(coord_one, search_object):
    assert search_object in get_sites(coord_one[0], coord_one[1], 100), 'not found'



