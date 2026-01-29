import os
from core.categories import CategoryService
from storage.json_storage import JsonStorage


def test_categories_persist_between_runs():
    """
    FR-18: Categories + Storage
    Категории должны сохраняться и загружаться.
    """
    filename = "test_categories.json"

    storage = JsonStorage(filename)
    categories = CategoryService(storage)

    categories.add_category("Health")

    # перезапуск
    storage_reloaded = JsonStorage(filename)
    categories_reloaded = CategoryService(storage_reloaded)

    assert "Health" in categories_reloaded.get_categories()

    os.remove(filename)
