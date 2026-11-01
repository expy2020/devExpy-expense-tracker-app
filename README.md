# 💰 Expense Tracker CLI

A command-line expense tracker built in Python. Records, displays, filters, summarizes, and persists personal expenses to a JSON file.

Built as **Project 1** of a self-directed 10-project Python roadmap, focused on learning by solving specific problems rather than following tutorials end-to-end.

---

## ✨ Features

- ➕ **Add expenses** with amount, category, and description
- 📋 **View all expenses** in a clean formatted table with auto-generated IDs
- 💵 **Calculate total spending**
- 🔎 **Filter expenses by category** (case-insensitive)
- 📊 **Category summary table** — totals per category, sorted highest-first
- 🏆 **Show largest expense** with its master-list ID
- 🗑️ **Delete expenses** by ID, with cancel option
- 💾 **Persistent storage** — saves to and loads from `expenses.json`
- ⚠️ **Robust loading** — validates data structure, migrates old formats, handles corruption gracefully
- 🛡️ **Backup on corruption** — damaged files are copied to `.bak` before being replaced
- 🧮 **Unsaved-changes detection** — compares current state to last-saved state, prompts on exit

---

## 🚀 Getting Started

### Requirements

- Python 3.10 or higher (uses modern f-string syntax)
- No external dependencies — standard library only

### Installation

```bash
git clone https://github.com/<your-username>/expense-tracker-cli.git
cd expense-tracker-cli
```

### Running

```bash
python main.py
```

That's it. First run starts with an empty list; a save file is created when you save.

---

## 📖 Usage

When you run the app, you'll see:

```
--- EXPENSES TRACKER ---
1. Add expense
2. Show all expenses
3. Show total expenses
4. Filter expenses by category
5. Show category summary table
6. Delete an expense
7. Save expenses (Manual)
8. Show largest expense
9. Exit
Enter your choice:
```

### Example session

```
Enter your choice: 1
--- ADD NEW EXPENSE ---
Enter expense description (e.g Eggs) : Lunch
Enter the amount: 2500.50
Enter the category(e.g. Food, Transportation): food
Successfully added: 'Lunch' under 'Food' ($2,500.50)

Enter your choice: 5

==============================
CATEGORY        | TOTAL SPENT
------------------------------
Food            | $2,500.50
==============================

Enter your choice: 7
Expenses saved successfully.

Enter your choice: 9
No changes to save. Exiting.
Goodbye!
```

---

## 🗂️ Data Format

Expenses are stored in `expenses.json`:

```json
[
  {
    "item": "Lunch",
    "amount": 2500.5,
    "category": "Food"
  },
  {
    "item": "Gym membership",
    "amount": 15000,
    "category": "Sport"
  }
]
```

### Notes on the format

- The file is **human-readable** — you can open it in any text editor.
- Older versions of this project used a `"description"` key. `load_expenses()` **automatically migrates** old files to the current `"item"` format on load. Your data won't break.
- If the file is corrupted or malformed, the app prints a warning, creates a `.bak` backup, and starts fresh rather than crashing.

---

## 🏗️ Project Structure

```
expense-tracker-cli/
├── main.py              # Entry point, menu loop, orchestration
├── storage.py           # Disk I/O: load_expenses, save_expenses, backup_file
├── helpers.py           # Pure logic: total, category_total, filter, has_changes
├── ui.py                # Terminal I/O: add_expense, show_all, delete, etc.
├── expenses.json        # Save file (created on first save)
├── expenses.json.bak    # Auto-created if expenses.json is corrupted
├── test_expense_tracker.py
└── README.md
```

### Separation of concerns

The project follows a strict four-layer split:

| File | Responsibility |
|---|---|
| `main.py` | Orchestration — wires the menu to functions, manages state |
| `storage.py` | File I/O — only this file opens `expenses.json` |
| `helpers.py` | Pure logic — no `input()`, no `print()`, no file access |
| `ui.py` | Terminal I/O — all `input()` and `print()` for user interaction |

**Dependency direction (no cycles):**

```
main.py    →  ui.py, helpers.py, storage.py
ui.py      →  helpers.py
storage.py →  (nothing)
helpers.py →  (nothing)
```

The `if __name__ == "__main__":` guard lives only in `main.py`. The other three files are libraries — importing them should not run the program.

---

## 🧠 Concepts Demonstrated

This project was built to practice:

- **Functions** — small, single-purpose, well-named
- **Separation of concerns** — four files, strict one-way dependencies
- **Parameters and returns** — passing data in, getting results out
- **Side-effect vs pure functions** — `add_expense` mutates; `total` returns
- **Data structures** — a list of dicts as the core data model
- **File I/O** — reading and writing with `with open(...)`
- **JSON serialization** — `json.dump` / `json.load`
- **Build-then-write safety** — serialization errors caught before file is truncated
- **Error handling** — `try` / `except` for `ValueError`, `IOError`, `FileNotFoundError`, `JSONDecodeError`
- **Defensive programming** — validating loaded data before trusting it
- **Schema migration** — upgrading old save files to the current format
- **File backup** — `shutil.copy2` for `.bak` recovery before replacing corrupt files
- **Load-once-at-startup** — a single in-memory source of truth; no re-reads that can destroy unsaved state
- **List comprehensions** — used in `filter_expenses_by_category`
- **Generator expressions** — used in `total()`
- **Set-based dict aggregation** — summing by category with `dict.get(key, 0)`
- **`lambda` and `sorted`** — sorting category totals and finding the largest expense
- **`enumerate` with `start=1`** — 1-based IDs for user display
- **1-based UI ↔ 0-based indexing** — the classic off-by-one conversion
- **Dirty-flag pattern** — tracking unsaved state, comparing in-memory to last-saved snapshot
- **Menu loop architecture** — `while True` + `if/elif/else` + `break`
- **`if __name__ == "__main__":` guard** — the file runs as a program but imports as a library

---

## 🔮 Future Improvements

Planned for later versions:

- [ ] Edit existing expenses
- [ ] Date field and filtering by date range
- [ ] Monthly and weekly report views
- [ ] CSV export
- [ ] Colored terminal output
- [ ] Sort options (by amount, date, category)
- [ ] Budget alerts
- [ ] Optional: convert to SQLite for larger datasets
- [ ] Optional: add `pytest` unit tests
- [ ] Optional: package as an installable CLI tool

---

## 🧪 Testing

Run the tests:

```bash
python test_expense_tracker.py
```

Expected output:

```
All tests passed
```

---

## 📝 Lessons Learned

A few things this project taught me:

- **Loading once at startup** keeps a single in-memory source of truth, avoiding data loss from reloading mid-session.
- **Renaming a key in your data model breaks existing files** — unless you write migration logic. Real software has to handle this.
- **Never mutate a list while iterating over it** — the index shifts under you and you skip items.
- **Defensive loading** turns "the app crashed" into "the app recovered."
- **A silent `continue` on invalid data is a black hole** — if you drop data, log why. Otherwise future-you spends an hour trying to find what disappeared.
- **Build-then-write** — `json.dumps()` into a string *before* opening the file in `"w"` mode. If serialization fails, the original file survives.
- **Stable IDs vs positional IDs** — `enumerate` IDs are fine when items never outlive a session. As soon as you ask a user to remember an ID across operations, you need IDs stored inside each dict, not derived from position.
- **The function's name must match its behavior** — if it takes the whole list, don't call it `show_expense` (singular).
- **Corrupted files deserve a backup.** Replacing a broken file with a fresh one is data loss. Copy the original to `.bak` first.
- **One disk read per run, one owner.** If two functions both call `load_expenses()`, they see two different copies of the same list. That leads to bugs that look like "why isn't my change showing up?" Give one function (usually `main`) sole ownership of the data, and pass it in as a parameter everywhere else.

---

## 📄 License

This project is for personal learning. Free to reference, learn from, and adapt.

---

## 🙏 Acknowledgements

Built as part of a self-directed 10-project Python roadmap focused on problem-solving over tutorial-following.#   d e v E x p y - e x p e n s e - t r a c k e r - a p p  
 