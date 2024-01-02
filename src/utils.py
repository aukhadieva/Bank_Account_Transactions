import json
import zipfile
from datetime import datetime


def load_zipfile():
    """
    Распаковывает файл.
    """
    with zipfile.ZipFile('/Users/dns/PycharmProjects/Bank_Account_Transactions/src/operations.zip') as zip_file:
        zip_file.extractall()


def load_operations():
    """
    Загружает операции в формате JSON и возвращает объекты Python.
    """
    with open('/Users/dns/PycharmProjects/Bank_Account_Transactions/src/operations.json') as file:
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
                          reverse=True)
    return sorted_list_


def change_date(sort_operations_):
    """
    Меняет формат даты на формат ДД.ММ.ГГГГ.
    Возвращает список с информацией о дате операции.
    """
    date_list = []
    for item in sort_operations_:
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
            split_numb = [iter(split_count[2])] * 4
            zip_numb = zip(*split_numb)
            count_numbers = [''.join(i) for i in zip_numb]
            stars1 = count_numbers[1][0:2] + "*" * (len(count_numbers[1]) - 2)
            stars2 = count_numbers[2].replace(count_numbers[2], '****')
            hide_number = ' '.join([split_count[0], split_count[1], count_numbers[0], stars1, stars2, count_numbers[3]])
            hide_from_list.append(hide_number)
        if len(split_count) == 2:
            if len(split_count[1]) == 16:
                split_numb = [iter(split_count[1])] * 4
                zip_numb = zip(*split_numb)
                count_numbers = [''.join(i) for i in zip_numb]
                stars1 = count_numbers[1][0:2] + "*" * (len(count_numbers[1]) - 2)
                stars2 = count_numbers[2].replace(count_numbers[2], '****')
                hide_number = ' '.join([split_count[0], count_numbers[0], stars1, stars2, count_numbers[3]])
                hide_from_list.append(hide_number)
            if len(split_count[1]) == 20:
                split_numb = [iter(split_count[1])] * 4
                zip_numb = zip(*split_numb)
                count_numbers = [''.join(i) for i in zip_numb]
                stars1 = count_numbers[1][0:2] + "*" * (len(count_numbers[1]) - 2)
                stars2 = count_numbers[2].replace(count_numbers[2], '****')
                stars3 = count_numbers[3].replace(count_numbers[3], '****')
                hide_number = ' '.join([split_count[0], count_numbers[0], stars1, stars2, stars3, count_numbers[4]])
                hide_from_list.append(hide_number)
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
        if item == 'Данные отсутствуют':
            hide_to_list.append('Данные отсутствуют')
        split_count = item.split(' ')
        if len(split_count) == 3:
            split_numb = [iter(split_count[2])] * 4
            zip_numb = zip(*split_numb)
            count_numbers = [''.join(i) for i in zip_numb]
            stars1 = count_numbers[1][0:2] + "*" * (len(count_numbers[1]) - 2)
            stars2 = count_numbers[2].replace(count_numbers[2], '****')
            hide_number = ' '.join([split_count[0], split_count[1], count_numbers[0], stars1, stars2, count_numbers[3]])
            hide_to_list.append(hide_number)
        if len(split_count) == 2:
            if len(split_count[1]) == 16:
                split_numb = [iter(split_count[1])] * 4
                zip_numb = zip(*split_numb)
                count_numbers = [''.join(i) for i in zip_numb]
                stars1 = count_numbers[1][0:2] + "*" * (len(count_numbers[1]) - 2)
                stars2 = count_numbers[2].replace(count_numbers[2], '****')
                hide_number = ' '.join([split_count[0], count_numbers[0], stars1, stars2, count_numbers[3]])
                hide_to_list.append(hide_number)
            if len(split_count[1]) == 20:
                split_numb = [iter(split_count[1])] * 4
                zip_numb = zip(*split_numb)
                count_numbers = [''.join(i) for i in zip_numb]
                stars1 = count_numbers[1][0:2] + "*" * (len(count_numbers[1]) - 2)
                stars2 = count_numbers[2].replace(count_numbers[2], '****')
                stars3 = count_numbers[3].replace(count_numbers[3], '****')
                hide_number = ' '.join([split_count[0], count_numbers[0], stars1, stars2, stars3, count_numbers[4]])
                hide_to_list.append(hide_number)
    return hide_to_list


def return_amount():
    """Возвращает список с информацией о сумме операции."""
    amount_list_ = []
    for item in sort_operations():
        amount = item["operationAmount"]["amount"]
        amount_list_.append(amount)
    return amount_list_
