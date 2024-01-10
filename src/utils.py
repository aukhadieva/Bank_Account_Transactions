import os
import json
import zipfile
from config import ROOT
from datetime import datetime


ZIP_PATH = os.path.join(ROOT, 'src', 'operations.zip')
JSON_PATH = os.path.join(ROOT, 'src', 'operations.json')


def load_zipfile():
    """
    Распаковывает файл.
    """
    with zipfile.ZipFile(ZIP_PATH) as zip_file:
        zip_file.extractall()


def load_operations():
    """
    Загружает операции в формате JSON и возвращает объекты Python.
    """
    with open(JSON_PATH) as file:
        operations = json.load(file)
        return operations


def sort_operations():
    """
    Сортирует даты в порядке убывания.
    Возвращает список словарей из пяти операций, отфильтрованных
    по дате (по убыванию) и со статусом EXECUTED.
    """
    operations_list = []
    for operation in load_operations():
        try:
            if operation['state'] == 'EXECUTED':
                operations_list.append(operation)
        except KeyError:
            pass
    sorted_list_ = sorted(operations_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
                          reverse=True) # lambda список переменных-аргументов: возвращаемое значение
    return sorted_list_[0:5]


def change_date():
    """
    Меняет формат даты на формат ДД.ММ.ГГГГ.
    Возвращает список с информацией о дате операции.
    """
    date_list = []
    for item in sort_operations():
        date_data = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
        date = f'{date_data:%d.%m.%Y}'
        date_list.append(date)
    return date_list


def return_description():
    """Возвращает список с описанием операции."""
    descriptions_list = []
    for item in sort_operations():
        description = item["description"]
        descriptions_list.append(description)
    return descriptions_list


def return_from():
    """Возвращает список с информацией номера карты/ счета отправителя."""
    list_from = []
    for item in sort_operations():
        try:
            data_from = item["from"]
            list_from.append(data_from)
        except KeyError:
            list_from.append('Данные отсутствуют')
    return list_from


def hide_from():
    """Скрывает номер карты/ счета отправителя."""
    hide_from_list = []
    for item in return_from():
        if item == 'Данные отсутствуют':
            hide_from_list.append('Данные отсутствуют')
        split_count = item.split(' ')
        if len(split_count) == 3:
            numb_stars = split_count[0], split_count[1], split_count[2][:4], split_count[2][5:7]+'**', '****', split_count[2][-4:]
            join_numb_stars = ' '.join(list(numb_stars))
            hide_from_list.append(join_numb_stars)
        if len(split_count) == 2:
            if len(split_count[1]) == 16:
                numb_stars = split_count[0], split_count[1][:4], split_count[1][5:7] + '**', '****', split_count[1][-4:]
                join_numb_stars = ' '.join(list(numb_stars))
                hide_from_list.append(join_numb_stars)
            if len(split_count[1]) == 20:
                numb_stars = split_count[0], split_count[1][:4], split_count[1][5:7] + '**', '**** ****', split_count[1][-4:]
                join_numb_stars = ' '.join(list(numb_stars))
                hide_from_list.append(join_numb_stars)
    return hide_from_list


def return_to():
    """Возвращает список с информацией номера карты/ счета получателя."""
    list_to = []
    for item in sort_operations():
        try:
            where = item["to"]
            list_to.append(where)
        except KeyError:
            list_to.append('Данные отсутствуют')
    return list_to


def hide_to():
    """Скрывает номер карты/ счета получателя."""
    hide_to_list = []
    for item in return_to():
        split_count = item.split(' ')
        numb_stars = split_count[0], '**' + split_count[1][-4:]
        join_numb_stars = ' '.join(list(numb_stars))
        hide_to_list.append(join_numb_stars)
    return hide_to_list


def return_amount():
    """Возвращает список с информацией о сумме операции."""
    amount_list_ = []
    for item in sort_operations():
        amount = item["operationAmount"]["amount"]
        amount_list_.append(amount)
    return amount_list_


def return_name():
    """Возвращает список с информацией о валюте операции."""
    currency_list = []
    for item in sort_operations():
        name = item["operationAmount"]["currency"]["name"]
        currency_list.append(name)
    return currency_list
