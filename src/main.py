from core.account import Account
from storage.json_storage import JsonStorage
from core.transactions import print_transactions_table,filter_by_category
from core.categories import CategoryService
from core.savings import SavingsService

def get_valid_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().upper()

        if choice in valid_choices:
            return choice

        print("❌ Invalid choice. Try again.")

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def main_menu(balance):
    print(f"""
💰 BALANCE: ${balance}

======== BUDGETPY ========
+  Add income
-  Add expense
TR  Show transactions
CAT  Categories
SAV  Savings
X  Exit
============================
""")

def main():
    storage = JsonStorage("data/finance_data.json")
    savings = SavingsService(storage)
    account = Account(storage)
    categories = CategoryService(storage)

    while True:
        main_menu(account.get_balance())
        choice = get_valid_choice(
            "Choose: ",
            {"+", "-", "TR", "CAT", "SAV", "X"}
        )

        if choice == "+":
            amount = get_valid_number("Amount: ")
            category = categories.choose_category()
            comment = input("Comment: ")
            account.add_income(amount, category, comment)
        elif choice == "-":
            amount = get_valid_number("Amount: ")
            category = categories.choose_category()
            comment = input("Comment: ")
            account.add_expense(amount, category, comment)
        elif choice == "TR":
            print_transactions_table(account.get_transactions())
        elif choice == "CAT":
            categories_menu(account, categories)
        elif choice == "SAV":
            savings_menu(savings)
        elif choice == "X":
            break

def categories_menu(account, categories_service):
    while True:
        transactions = account.get_transactions()
        categories = categories_service.get_categories()

        print("\n📂 Categories")
        for i, cat in enumerate(categories, start=1):
            total = categories_service.category_total(transactions, cat)
            print(f"{i}. {cat.ljust(15)} | {total}")

        print(f"{len(categories) + 1}.  Add category")
        print("0. Back")

        valid_choices = {str(i) for i in range(len(categories) + 2)}
        choice = get_valid_choice("Choose: ", valid_choices)

        if choice == "0":
            break

        # ➕ Add category
        elif choice == str(len(categories) + 1):
            name = input("Category name: ")
            try:
                categories_service.add_category(name)
                print("✅ Category added")
            except ValueError as e:
                print(f"❌ {e}")

        # 📂 Open category
        else:
            try:
                index = int(choice) - 1
                category = categories[index]

                print(f"\n📄 Category: {category}\n")
                filtered = filter_by_category(transactions, category)
                print_transactions_table(filtered)

                input("\nPress Enter to go back...")

            except (ValueError, IndexError):
                print("❌ Invalid choice")

def savings_menu(savings_service):
    while True:
        savings = savings_service.get_savings()

        print("\n💰 Savings")
        for i, s in enumerate(savings, start=1):
            print(
                f"{i}. {s['name'].ljust(15)} | "
                f"{s['current']} / {s['target']}"
            )

        print(f"{len(savings) + 1}. Add saving")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "0":
            break

        elif choice == str(len(savings) + 1):
            name = input("Saving name: ")
            target = get_valid_number("Target Amount: ")
            savings_service.add_saving(name, target)
            print("✅ Saving created")

        else:
            try:
                index = int(choice) - 1
                saving = savings[index]

                print(f"\n🎯 {saving['name']}")
                print(f"Saved: {saving['current']}")
                print(f"Target: {saving['target']}")
                print(f"Remaining: {saving['target'] - saving['current']}")

                action = input("\n+ Add money | 0 Back: ")

                if action == "+":
                    amount = get_valid_number("Amount: ")
                    savings_service.add_money(index, amount)
                    print("✅ Money added")

            except (ValueError, IndexError):
                print("❌ Invalid choice")

if __name__ == "__main__":
    main()