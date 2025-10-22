# Expenses Tracker Project

import csv
from datetime import datetime

expenses = []

def add_expense(description, amount, category="General"):
    # Adds an expense with description, amount, category, and timestamp
    expense = {
        "description": description,
        "amount": round(float(amount), 2),
        "category": category,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    print("Expense added successfully!")

def list_expenses():
    #Prints all recorded expenses in a table format
    if not expenses:
        print(" No expenses recorded yet")
        return
    print("\n---Expense Log ---")
    print(f"{'Description':<15}{'amount':<10}{'Category':<12}{'Timestamp'}")
    print("-" * 70)
    for index, exp in enumerate(expenses, 1):
        print(f"{index}. {exp['description']} | ${exp['amount']} | {exp['category']} "
              f"| {exp['timestamp']}")

def total_expenses():
    #Returns the total sum of expenses
    total = sum(exp['amount'] for exp in expenses)
    print(f"\n Total Expenses: ${total:.2f}")

def export_to_csv(filename="expenses.csv"):
    # Exports expenses to a csv file
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["description", "amount",
                                                  "category", "timestamp"])
        writer.writeheader()
        writer.writerows(expenses)

def main():
    while True:
        choice = input("\nChoose an action: [a]Add, [b]List, [c]Total, [d]Export, [e]Quit: ").lower()

        if choice == "a":
            desc = input("Enter Description: ")
            amt = float(input("Enter Amount: "))
            cat = input("Enter Category: ")
            add_expense(desc, amt, cat)
        elif choice == "b":
            list_expenses()
        elif choice == "c" :
            total_expenses()
        elif choice == "d":
            filename = input("Enter filename (e.g., expenses.csv): ")
            export_to_csv(filename)
            print(f"Expenses exported to {filename}")
        elif choice == "e":
            print("Exiting Expense Tracker. Goodbye")
            break
        else:
            print("Invalid Choice, try again. ")

if __name__ == "__main__":
    main()

