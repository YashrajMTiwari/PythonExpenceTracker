import os

FILE_NAME = "expenses.txt"

def log_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Travel, Utilities): ")
    description = input("Enter a short description of the expense: ")
    amount = float(input("Enter the amount: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{description},{amount}\n")

    print("Expense logged successfully!")

def display_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    total = 0.0
    category_totals = {}

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, description, amount = line.strip().split(',')
            amount = float(amount)
            total += amount

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\nSummary of Expenses:")
    print(f"Total Expenses: ${total:.2f}")
    print("Expenses by Category:")
    for category, amount in category_totals.items():
        print(f" - {category}: ${amount:.2f}")

def display_all_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    print("\nAll Recorded Expenses:")
    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, description, amount = line.strip().split(',')
            print(f"Date: {date}, Category: {category}, Description: {description}, Amount: ${amount}")

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Log an expense")
        print("2. View summary of expenses")
        print("3. View all expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_expense()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            display_all_expenses()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
