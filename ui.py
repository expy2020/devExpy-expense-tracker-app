from helpers import category_total

def add_expense(expenses):
    print("\n--- ADD NEW EXPENSE ---")

    
    item = input("Enter expense description (e.g Eggs) : ").strip()
    while not item:
        print("Description cannot be empty. Please enter a valid description.")
        item = input("Enter expense description: ").strip()


    while True:
        try:
            amount = float(input("Enter the amount: ").strip())
            if amount <= 0:
                print("Amount must be greater than zero. Try again.")
                continue
            break
        except ValueError:
            print("That's not a number. Try again.")
            
 
    category = input("Enter the category(e.g. Food, Transportation): ").strip().title()    
    if not category:
        category = "Uncategorized"  # Default category if none provided/if they hit Enter

    expense = {
            "item": item,
            "amount": amount,
            "category": category,
        }
    expenses.append(expense)
    # print(expenses)
    print(f"Successfully added: '{item}' under '{category}' (${amount:,.2f})")
# add_expense(expenses)

def show_expense(index, expense):
    # print(f"{expense ['category']} | {expense ['amount']} | {expense ['description']}")
    amount_text = f"${expense['amount']:,.2f}"
    print(f"{index:<15} {expense['category']:<20} {amount_text:<20} {expense['item']}")
    
def show_all(expenses, preindexed=False):
    print("-" * 75)
    print(f"{'ID':<15} {'Category':<20} {'Amount':<20} {'Item'}")
    print("-" * 75)
    if preindexed:
        for index, expense in expenses:
            show_expense(index, expense)
    else:
        for index, expense in enumerate(expenses, 1):
            show_expense(index, expense)

    print("-" * 75)    

# show_all(expenses)

    
def delete_expenses(expenses):
    if not expenses:
        print("No expenses to delete.")
        return False  # No expenses to delete, return False to indicate no changes
    
    show_all(expenses)
    print("(Type 0 to cancel and go back.)")
    while True:
        try:
            choice = input("Enter the number of expense to delete: ")
            if choice == "0":
                print("Deletion cancelled.")
                return False  # Deletion cancelled, return False to indicate no changes

            expense_to_delete = int(choice) - 1  # Adjust for 0-based index
            if 0 <= expense_to_delete < len(expenses):
                deleted_expense = expenses.pop(expense_to_delete)
                print(f"Deleted expense: {deleted_expense}")
                return True # Return True to indicate that changes were made
            else:
                print("Index out of range. Try again.")
        except (ValueError): 
            print("Invalid input. Please enter a valid index.")

def show_largest_expense(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    # largest_expense = max(expenses, key=lambda x: x["amount"], default=None)
    # original_index = expenses.index(largest_expense) + 1
    largest_pair = [max(enumerate(expenses, 1), key=lambda x: x[1]["amount"])]
    print("\n--- LARGEST EXPENSE ---")
    show_all(largest_pair, preindexed=True)

def show_summary(expenses):
    if not expenses:
        print("No expenses recorded to summarize.")
        return
    totals = category_total(expenses)
    sorted_total = sorted(totals.items(), key = lambda x: x[1], reverse=True)
    print("\n==============================")
    print(f"{'CATEGORY':<15} | {'TOTAL SPENT':<12}")
    print("------------------------------") 
    for cat, total_amount in sorted_total:
        print(f"{cat:<15} | ${total_amount:<12,.2f}")
    print("=" * 30)        