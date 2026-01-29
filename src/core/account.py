from models.transaction import Transaction


class Account:
    def __init__(self, storage, initial_balance=0):
        self.storage = storage

        # Загружаем данные из хранилища
        data = self.storage.load() or {}

        is_new = False

        # Инициализация баланса только при первом создании
        if "balance" not in data:
            data["balance"] = initial_balance
            is_new = True

        # Инициализация списка транзакций
        if "transactions" not in data:
            data["transactions"] = []
            is_new = True

        self.data = data

        # Сохраняем ТОЛЬКО если данные инициализируются впервые
        if is_new:
            self.storage.save(self.data)

    def add_income(self, amount, category, comment):
        if amount <= 0:
            return False

        t = Transaction("income", amount, category, comment)
        self.data["transactions"].append(t.to_dict())
        self.data["balance"] += amount
        self.storage.save(self.data)
        return True

    def add_expense(self, amount, category, comment):
        if amount <= 0 or amount > self.data["balance"]:
            return False

        t = Transaction("expense", -abs(amount), category, comment)
        self.data["transactions"].append(t.to_dict())
        self.data["balance"] -= abs(amount)
        self.storage.save(self.data)
        return True

    def get_balance(self):
        return self.data["balance"]

    def get_transactions(self):
        return self.data["transactions"]
