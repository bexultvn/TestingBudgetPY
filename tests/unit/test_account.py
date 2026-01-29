import pytest
from core.account import Account


def test_create_account_with_initial_balance(account):
    """
    FR-1: Система должна позволять создавать счёт
    с начальным балансом.
    """
    assert account.get_balance() == 1000


def test_add_income_increases_balance(account):
    """
    FR-2: Система должна позволять пополнять баланс.
    """
    result = account.add_income(300, "Salary", "January salary")

    assert result is True
    assert account.get_balance() == 1300


def test_add_expense_with_sufficient_balance(account):
    """
    FR-3: Система должна позволять снимать средства
    при достаточном балансе.
    """
    result = account.add_expense(400, "Food", "Dinner")

    assert result is True
    assert account.get_balance() == 600


def test_add_expense_with_insufficient_balance(fake_storage):
    """
    FR-4: Система не должна позволять снимать сумму,
    превышающую текущий баланс.
    """
    account = Account(fake_storage, initial_balance=200)
    result = account.add_expense(500, "Rent", "Monthly rent")

    assert result is False
    assert account.get_balance() == 200


# ------------------------------------------------------------------
# Parametrized tests (negative & edge cases)
# ------------------------------------------------------------------

@pytest.mark.parametrize(
    "amount",
    [-100]
)
def test_add_income_negative_amount(account, amount):
    """
    FR-2 (negative):
    Нельзя пополнять баланс отрицательной суммой.
    """
    result = account.add_income(amount, "Salary", "Invalid")

    assert result is False
    assert account.get_balance() == 1000


@pytest.mark.parametrize(
    "amount",
    [0, 999_000_000]
)
def test_add_income_edge_cases(account, amount):
    """
    FR-2 (edge cases):
    Граничные значения пополнения баланса.
    """
    result = account.add_income(amount, "Salary", "Edge")

    if amount == 0:
        assert result is False
        assert account.get_balance() == 1000
    else:
        assert result is True
        assert account.get_balance() == 1000 + amount


@pytest.mark.parametrize(
    "amount",
    [-100, 0, 999_000_000]
)
def test_add_expense_invalid_and_edge_cases(account, amount):
    """
    FR-4:
    Некорректные и граничные случаи снятия средств.
    """
    result = account.add_expense(amount, "Food", "Invalid")

    assert result is False
    assert account.get_balance() == 1000
