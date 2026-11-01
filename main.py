from storage import load_expenses, save_expenses
from helpers import total, filter_expenses_by_category, has_changes
from ui import add_expense, show_all, show_summary, delete_expenses, show_largest_expense
import copy

def main():
    expenses = load_expenses()
    last_saved_state  = copy.deepcopy(expenses)
    while True:
        print("\n--- EXPENSES TRACKER ---")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Show total expenses")
        print("4. Filter expenses by category")  
        print("5. Show category summary table")
        print("6. Delete an expense")
        print("7. Save expenses (Manual)")
        print("8. Show largest expense")
        print("9. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_all(expenses)
        elif choice == "3":
            result = total(expenses)
            print(f"Total expenses: ${result:,.2f}")
        elif choice == "4":
            while True:
                category = input("Enter category name to filter by: ").strip()
                filtered_category = filter_expenses_by_category(expenses, category)
            
                if filtered_category:
                    print(f"\n--- Expenses matching '{category}' ---")
                    print("(IDs match the master list — use these to delete)")
                    show_all(filtered_category, preindexed=True)
                    break   
                else:
                    print(f"No expenses found matching the category '{category}'. Try again.")    
        elif choice == "5":
            show_summary(expenses)
        elif choice == "6":
            delete_expenses(expenses)  
        elif choice == "7":
            save_expenses(expenses) 
            last_saved_state = copy.deepcopy(expenses)  # Update the last saved state
            print("Expenses saved successfully.")
        elif choice == "8":
            show_largest_expense(expenses)
        elif choice == "9":
            if has_changes(expenses, last_saved_state):
                while True:
                    confirm = input("You have unsaved changes. Save before exiting? (y/n): ").strip().lower()
                    if confirm == "y":
                        save_expenses(expenses)
                        print("Expenses saved successfully.")
                        break
                    elif confirm == "n":
                        print("Exiting without saving changes.")
                        break
                    print("Please enter 'y' or 'n'.")
            else:
                print("No changes to save. Exiting.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


def has_changes(expenses, last_saved_state):
    return expenses != last_saved_state  # Compare current state with last saved state           

if __name__ == "__main__":
    main()