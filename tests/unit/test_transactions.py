import pytest


@pytest.mark.parametrize(
    "initial_balance, action, amount, category, expected_amount",
    [
        # income transaction
        (0, "income", 1000, "Salary", 1000),

        # expense transaction
        (1000, "expense", 200, "Food", -200),
    ]
)
def test_transaction_is_saved(
    account_factory,
    initial_balance,
    action,
    amount,
    category,
    expected_amount
):
    """
    FR-5:
    Система должна сохранять транзакции
    с указанием суммы и категории (income и expense).
    """
    account = account_factory(initial_balance)

    if action == "income":
        account.add_income(amount, category, "Test income")
    else:
        account.add_expense(amount, category, "Test expense")

    transactions = account.get_transactions()

    assert len(transactions) == 1
    assert transactions[0]["amount"] == expected_amount
    assert transactions[0]["category"] == category
