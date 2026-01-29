import os
from storage.json_storage import JsonStorage


def test_save_data_to_json_file():
    """
    FR-14: Система должна сохранять данные в JSON-файл.
    """
    filename = "test_storage.json"
    storage = JsonStorage(filename)

    data = {
        "balance": 1000,
        "transactions": [],
        "categories": ["Food"]
    }

    storage.save(data)

    assert os.path.exists(filename)

    os.remove(filename)

def test_load_data_from_json_file():
    """
    FR-15: Система должна загружать данные
    из JSON-файла при запуске приложения.
    """
    filename = "test_storage.json"
    storage = JsonStorage(filename)

    data = {
        "balance": 500,
        "transactions": [],
        "categories": ["Transport"]
    }

    storage.save(data)
    loaded_data = storage.load()

    assert loaded_data == data

    os.remove(filename)