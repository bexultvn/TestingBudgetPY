import pytest


def test_create_saving_goal(savings_service):
    """
    FR-7: Система должна позволять создавать
    цель накопления с целевой суммой.
    """
    savings_service.add_saving("Laptop", 1000)

    savings = savings_service.get_savings()
    assert len(savings) == 1
    assert savings[0]["name"] == "Laptop"
    assert savings[0]["target"] == 1000
    assert savings[0]["current"] == 0


@pytest.mark.parametrize(
    "amount, expected_current",
    [
        (500, 500),           # normal case
        (0, 0),               # edge case
        (-100, 0),            # negative case
        (999_000_000, 999_000_000),  # realistic upper bound
    ]
)
def test_add_money_to_saving_parametrized(savings_service, amount, expected_current):
    """
    FR-8, FR-9:
    Добавление средств в копилку (normal, edge, negative cases).
    """
    savings_service.add_saving("Vacation", 2_000_000_000)
    savings_service.add_money(0, amount)

    savings = savings_service.get_savings()
    assert savings[0]["current"] == expected_current
