from core.account import Account
from storage.json_storage import JsonStorage


def test_account_persistence_between_runs(tmp_path):
    """
    FR-16: Account + Storage
    Баланс и транзакции должны сохраняться
    и восстанавливаться после перезапуска.
    """
    file_path = tmp_path / "account.json"

    storage = JsonStorage(file_path)
    account = Account(storage, initial_balance=1000)

    account.add_income(500, "Salary", "April")
    account.add_expense(200, "Food", "Dinner")

    # имитация перезапуска приложения
    storage_reloaded = JsonStorage(file_path)
    account_reloaded = Account(storage_reloaded)

    assert account_reloaded.get_balance() == 1300
    assert len(account_reloaded.get_transactions()) == 2


def test_account_uses_same_storage_instance(tmp_path):
    """
    FR-17: Account должен корректно работать
    с хранилищем данных.
    """
    file_path = tmp_path / "account2.json"

    storage = JsonStorage(file_path)
    account = Account(storage, initial_balance=300)

    account.add_income(200, "Bonus", "Work")

    data = storage.load()
    assert data["balance"] == 500
