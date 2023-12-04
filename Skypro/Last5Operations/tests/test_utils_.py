from tests.conftest import utils_fix

from utils.utils_ import read_json, search_executed, sort_executed, edit_date, secret_numb


def test_read_json():
    operations = read_json()
    assert read_json()[0]['id'] == 441945886
    assert read_json()[0]['date'] == "2019-08-26T10:50:58.294041"
    assert len(operations) == 101

def test_search_executed(utils_fix):
    assert search_executed(utils_fix) == [{
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472"
    },
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907"
    }]


def test_edit_date():
    assert edit_date('2018-04-14T19:35:28.978265') == '14.04.2018'
    assert edit_date('2018-09-12T21:27:25.241689') == '12.09.2018'

def test_secret_numb():
    assert secret_numb('3152479541115065') == '3152 47** **** 5065'
    assert secret_numb('3152479541115065', to=True) == '** 5065'


def test_sort_executed(utils_fix):
    assert sort_executed(utils_fix) == [{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
    },
    {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
        "amount": "67314.70",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
    },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        }
    ]