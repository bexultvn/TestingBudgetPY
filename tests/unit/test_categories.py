import pytest


def test_add_new_category(category_service):
    """
    FR-11: Система должна позволять создавать
    пользовательские категории.
    """
    category_service.add_category("Health")

    categories = category_service.get_categories()
    assert "Health" in categories


def test_add_duplicate_category_raises_error(category_service):
    """
    FR-12: Система не должна позволять создавать
    дублирующиеся категории.
    """
    with pytest.raises(ValueError):
        category_service.add_category("Food")


def test_default_categories_created(category_service):
    """
    FR-13: Система должна позволять получать
    список всех доступных категорий.
    """
    categories = category_service.get_categories()

    assert categories == [
        "Food",
        "Transport",
        "Subscriptions",
        "Entertainment"
    ]


@pytest.mark.parametrize(
    "category, expected_total",
    [
        ("Food", -150),
        ("Transport", -200),
        ("Entertainment", 0),  # edge case: нет транзакций
    ]
)
def test_category_total_sum_parametrized(category_service, category, expected_total):
    """
    Система должна корректно считать
    сумму транзакций по категории.
    """
    transactions = [
        {"amount": -100, "category": "Food"},
        {"amount": -50, "category": "Food"},
        {"amount": -200, "category": "Transport"},
    ]

    total = category_service.category_total(transactions, category)

    assert total == expected_total
