import zipfile


def load_zipfile():
    """
    Распаковывает файл.
    """
    with zipfile.ZipFile('/Users/dns/PycharmProjects/Bank_Account_Transactions/src/operations.zip') as zip_file:
        zip_file.extractall()
