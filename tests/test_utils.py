import pytest

from src import utils

path = r'C:\Users\Тоир\PycharmProjects\cw_3\src\operations.json'


@pytest.fixture
def get_operations():
    return utils.get_last_operations(utils.get_clear_data(utils.load_data(path)), 2)


def test_get_last_operations(get_operations):
    assert len(get_operations) == 2
    assert get_operations == [
        {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
         'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'},
        {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}]


def test_get_datetime(get_operations):
    assert utils.get_datetime(utils.get_last_operations(get_operations, 2)) == ['07.12.2019', '08.12.2019']


def test_get_description_operations(get_operations):
    assert utils.get_description_operations(get_operations) == ['Перевод организации', 'Открытие вклада']


def test_get_transfer_from(get_operations):
    assert utils.get_transfer_from(get_operations) == ['Visa Classic 2842878893689012', None]


def test_get_transfer_to(get_operations):
    assert utils.get_transfer_to(get_operations) == ['Счет 35158586384610753655', 'Счет 90424923579946435907']


def test_get_operation_amount(get_operations):
    assert utils.get_operation_amount(get_operations) == ['48150.39', '41096.24']


def test_get_operation_currency(get_operations):
    assert utils.get_operation_currency(get_operations) == ['USD', 'USD']


def test_hide_card_number_sender(get_operations):
    assert utils.hide_card_number_sender(utils.get_transfer_from(get_operations)) == [
        'Visa Classic 2842 87** **** 9012',
        'Неизвестный отправитель']


def test_hide_card_number_payee(get_operations):
    assert utils.hide_card_number_payee(utils.get_transfer_to(get_operations)) == ['Счет **3655', 'Счет **5907']
