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
