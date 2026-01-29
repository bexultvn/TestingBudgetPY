from datetime import datetime

class Transaction:
    def __init__(self, t_type, amount, category, comment=""):
        self.type = t_type
        self.amount = amount
        self.category = category
        self.comment = comment
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "type": self.type,
            "amount": self.amount,
            "category": self.category,
            "comment": self.comment,
            "date": self.date
        }