import os
from core.savings import SavingsService
from storage.json_storage import JsonStorage
from core.account import Account


def test_savings_persistence_between_runs():
    """
    FR-19: Savings + Storage
    Копилки должны сохраняться и загружаться.
    """
    filename = "test_savings.json"

    storage = JsonStorage(filename)
    savings = SavingsService(storage)

    savings.add_saving("Laptop", 1500)
    savings.add_money(0, 400)

    # перезапуск
    storage_reloaded = JsonStorage(filename)
    savings_reloaded = SavingsService(storage_reloaded)

    saved = savings_reloaded.get_savings()
    assert saved[0]["name"] == "Laptop"
    assert saved[0]["current"] == 400

    os.remove(filename)


def test_multiple_save_load_cycles(tmp_path):
    """
    FR-20: Данные должны оставаться целостными
    при многократной записи и чтении.
    """
    file_path = tmp_path / "savings.json"

    storage = JsonStorage(file_path)
    account = Account(storage, initial_balance=100)
    savings = SavingsService(storage)

    savings.add_saving("Phone", 500)
    savings.add_money(0, 100)

    # первый перезапуск
    storage_reloaded = JsonStorage(file_path)
    savings_reloaded = SavingsService(storage_reloaded)
    savings_reloaded.add_money(0, 150)

    final_savings = savings_reloaded.get_savings()

    assert final_savings[0]["current"] == 250
