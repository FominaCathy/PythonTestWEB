from api_utils import test_check


def test_valid(valid_text, invalid_text):
    assert valid_text in test_check(invalid_text)
