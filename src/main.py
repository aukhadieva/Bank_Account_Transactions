from src.utils import (load_zipfile, sort_operations, change_date, return_description, hide_from, hide_to,
                       return_amount, return_name)


def show_transactions():
    """
    Выводит на экран список из n последних выполненных клиентом операций в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>.
    """
    sort_operations_ = sort_operations()[0:int(input('Привет! Выбери количество операций, '
                                                     'информацию по которым ты хочешь просмотреть:\n'))]
    for date, description, from_, to_, amount, name in zip(change_date(sort_operations_), return_description(),
                                                           hide_from(), hide_to(), return_amount(), return_name()):
        print(f'{date} {description}\n{from_} --> {to_}\n{amount} {name}\n')


load_zipfile()
show_transactions()
