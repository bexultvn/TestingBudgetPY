def print_transactions_table(transactions):
    if not transactions:
        print("\n📭 No transactions found\n")
        return

    headers = ["ID", "AMOUNT", "TYPE", "CATEGORY", "DATE"]

    col_widths = {
        "ID": 4,
        "AMOUNT": 12,
        "TYPE": 6,
        "CATEGORY": 15,
        "DATE": 12
    }

    def separator():
        print("-" * sum(col_widths.values()))

    # header
    print(
        headers[0].ljust(col_widths["ID"]) +
        headers[1].ljust(col_widths["AMOUNT"]) +
        headers[2].ljust(col_widths["TYPE"]) +
        headers[3].ljust(col_widths["CATEGORY"]) +
        headers[4].ljust(col_widths["DATE"])
    )
    separator()

    for i, transaction in enumerate(transactions, start=1):
        amount = abs(transaction["amount"])
        tx_type = " +" if transaction["amount"] > 0 else " -"
        date = transaction["date"].split(" ")[0]
        comment = transaction.get("comment", "").strip()

        # main row
        print(
            str(i).ljust(col_widths["ID"]) +
            str(amount).ljust(col_widths["AMOUNT"]) +
            tx_type.ljust(col_widths["TYPE"]) +
            transaction["category"].ljust(col_widths["CATEGORY"]) +
            date.ljust(col_widths["DATE"])
        )

        # comment row
        if comment:
            print(f"    ({comment})")

        print()


def filter_by_category(transactions, category):
    return [t for t in transactions if t["category"] == category]
