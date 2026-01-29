class CategoryService:
    def __init__(self, storage):
        self.storage = storage
        self.data = self.storage.load()

        if "categories" not in self.data:
            self.data["categories"] = [
                "Food",
                "Transport",
                "Subscriptions",
                "Entertainment"
            ]
            self.storage.save(self.data)

    def get_categories(self):
        return self.data["categories"]

    def add_category(self, name):
        if name in self.data["categories"]:
            raise ValueError("Category already exists")

        self.data["categories"].append(name)
        self.storage.save(self.data)

    def choose_category(self):
        categories = self.get_categories()

        print("\nSelect category:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        choice = int(input("Number: "))
        return categories[choice - 1]

    def category_total(self, transactions, category):
        return sum(
            transaction["amount"]
            for transaction in transactions
            if transaction["category"] == category
        )
