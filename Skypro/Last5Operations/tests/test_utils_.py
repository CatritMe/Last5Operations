from utils.utils_ import get_from_json


def test_get_from_json():
    assert get_from_json()[0]['id'] == 441945886