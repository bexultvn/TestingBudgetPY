import pytest
from core.account import Account
from core.savings import SavingsService
from core.categories import CategoryService

class FakeStorage:
    def __init__(self):
        self.data = {}

    def load(self):
        return self.data

    def save(self, data):
        self.data = data


@pytest.fixture
def fake_storage():
    return FakeStorage()


@pytest.fixture
def account(fake_storage):
    return Account(fake_storage, initial_balance=1000)


@pytest.fixture
def savings_service(fake_storage):
    return SavingsService(fake_storage)


@pytest.fixture
def category_service(fake_storage):
    return CategoryService(fake_storage)


@pytest.fixture
def account_factory(fake_storage):
    def _create(initial_balance):
        return Account(fake_storage, initial_balance=initial_balance)
    return _create

