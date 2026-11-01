import json
import os


FILENAME = "expenses.json"
def save_expenses(expenses):
    try:
        with open(FILENAME, "w") as f:
            json.dump(expenses, f, indent=2)
    except IOError as e:
        print(f"Error saving expenses: {e}")

def load_expenses():
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r") as file:
            data = json.load(file)
            
        # Robustness Check 1: Ensure top-level structure is a list
        if not isinstance(data, list):
            print("\n⚠️ Warning: 'expenses.json' structure is invalid (expected a list). Starting fresh.")
            return []
        validated_expenses = []
        for expense in data:
            # Robustness Check 2: Validate dictionary items and required fields
            if isinstance(expense, dict) and "amount" in expense:
                
                # Protect against key migration (forces everything into your 'item' key)
                if "item" not in expense and "description" in expense:
                    expense["item"] = expense["description"]
                elif "item" not in expense:
                    expense["item"] = "No Description"
                    
                if "category" not in expense:
                    expense["category"] = "Uncategorized"
                else:
                    expense["category"] = expense["category"].strip().title()  # Normalize category capitalization    
                    
                # Clean up the old key if it exists so you don't save redundant data
                expense.pop("description", None)
                    
                validated_expenses.append(expense) 
            else:
                print("\n⚠️ Skipping a corrupted or incomplete expense entry.")  

        return validated_expenses         
    except (json.JSONDecodeError, IOError):
        print("\n⚠️ Warning: Could not read 'expenses.json' properly. Starting fresh.")
        return []   
