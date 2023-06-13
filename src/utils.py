import json
from datetime import datetime
from operator import itemgetter


def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_clear_data(operations):
    clear_data = []
    for operation in operations:
        if not operation:
            continue
        else:
            clear_data.append(operation)
    return sorted(clear_data, key=itemgetter('date'))


def get_last_operations(operations, user_input):
    executed_operations = []
    for operation in operations:
        if operation.get('state') == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations[-user_input:]


def get_datetime(executed_operations):
    date_time = []
    for operation in executed_operations:
        date_time.append(datetime.strptime(operation["date"], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y'))
    return date_time


def get_description_operations(executed_operations):
    descriptions = []
    for operation in executed_operations:
        descriptions.append(operation["description"])
    return descriptions


def get_transfer_from(executed_operation):
    transfers_from = []
    for operation in executed_operation:
        transfers_from.append(operation.get("from"))
    return transfers_from


def get_transfer_to(executed_operations):
    transfers_to = []
    for operation in executed_operations:
        transfers_to.append(operation["to"])
    return transfers_to


def get_operation_amount(executed_operations):
    operations_amount = []
    for operation in executed_operations:
        operations_amount.append(operation["operationAmount"]["amount"])
    return operations_amount


def get_operation_currency(executed_operations):
    operations_currency = []
    for operation in executed_operations:
        operations_currency.append(operation["operationAmount"]["currency"]["name"])
    return operations_currency


def hide_card_number_sender(transfer_from):
    hidden_number_card_sender = []
    for operation in transfer_from:
        if not operation:
            hidden_number_card_sender.append('Неизвестный отправитель')
        elif len(operation.split()) == 3:
            hidden_number_card_sender.append(f'{operation.split()[0]} {operation.split()[1]} '
                                             f'{operation.split()[2][:4]} {operation.split()[2][4:6]}** **** '
                                             f'{operation.split()[2][-4:]}')
        else:
            hidden_number_card_sender.append(
                f'{operation.split()[0]} {operation.split()[1][:4]} {operation.split()[1][4:6]}** ****'
                f' {operation.split()[1][-4:]}')

    return hidden_number_card_sender


def hide_card_number_payee(transfer_to):
    hidden_number_card_payee = []
    for operation in transfer_to:
        if len(operation.split()) == 3:
            hidden_number_card_payee.append(f'{operation.split()[0]} {operation.split()[1]} '
                                            f'**{operation.split()[2][-4:]}')
        else:
            hidden_number_card_payee.append(f'{operation.split()[0]} **{operation.split()[1][-4:]}')
    return hidden_number_card_payee
