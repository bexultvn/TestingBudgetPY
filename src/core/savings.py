class SavingsService:
    def __init__(self, storage):
        self.storage = storage

        data = self.storage.load() or {}

        is_new = False

        if "savings" not in data:
            data["savings"] = []
            is_new = True

        self.data = data

        # сохраняем только при первой инициализации
        if is_new:
            self.storage.save(self.data)

    def get_savings(self):
        return self.data["savings"]

    def add_saving(self, name, target):
        if target <= 0:
            return False

        saving = {
            "name": name,
            "target": target,
            "current": 0
        }

        self.data["savings"].append(saving)
        self.storage.save(self.data)
        return True

    def add_money(self, index, amount):
        #  КРИТИЧЕСКАЯ ВАЛИДАЦИЯ
        if amount <= 0:
            return False

        self.data["savings"][index]["current"] += amount
        self.storage.save(self.data)
        return True
