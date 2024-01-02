import json
import zipfile


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
