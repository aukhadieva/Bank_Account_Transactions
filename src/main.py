from src.utils import (load_zipfile, change_date, return_description, hide_from, hide_to,
                       return_amount, return_name)


def show_transactions():
    """
    Выводит на экран список из n последних выполненных клиентом операций в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>.
    """
    for date, description, from_, to_, amount, name in zip(change_date(), return_description(),
                                                           hide_from(), hide_to(), return_amount(), return_name()):
        print(f'{date} {description}\n{from_} -> {to_}\n{amount} {name}\n')


load_zipfile()
show_transactions()
