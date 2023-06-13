import utils


def main():
    data = utils.load_data('operations.json')
    operations = utils.get_clear_data(data)

    user_input = int(input('Введите количество последних операций, которые хотите увидеть: '))

    executed_operations = utils.get_last_operations(operations, user_input)
    date = utils.get_datetime(executed_operations)
    description = utils.get_description_operations(executed_operations)
    sender = utils.hide_card_number_sender(utils.get_transfer_from(executed_operations))
    payee = utils.hide_card_number_payee(utils.get_transfer_to(executed_operations))
    amount = utils.get_operation_amount(executed_operations)
    currency = utils.get_operation_currency(executed_operations)

    for i in range(user_input):
        print(f'{date[i]} {description[i]}\n'
              f'{sender[i]} > {payee[i]}\n'
              f'{amount[i]} {currency[i]}')
        print()


if __name__ == '__main__':
    main()
