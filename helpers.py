
def total(expenses):
    return sum(expense["amount"] for expense in expenses)

def filter_expenses_by_category(expenses, category):
    if not expenses:
        print("No expenses recorded yet.")
        return
    filtered_expenses = [
        (index, expense)
        for index, expense in enumerate(expenses, 1)
        if expense.get("category", "Uncategorized").strip().title() == category.strip().title()
        ]
    return filtered_expenses

def category_total(expenses):
    totals = {}
    for expense in expenses:
        cat = expense.get("category", "Uncategorized").strip().title()
        amount = expense.get("amount", 0)
        totals[cat] = totals.get(cat, 0) + amount
    return totals

def has_changes(expenses, last_saved_state):
    return expenses != last_saved_state  # Compare current state with last saved state   