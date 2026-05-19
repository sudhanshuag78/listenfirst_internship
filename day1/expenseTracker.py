import json


try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

except:
    expenses = []


while True:

    print("\n1. Add Expense")
    print("2. View Expense")
    print("3. Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        title = input("Enter title: ")
        amount = int(input("Enter amount: "))

        expense = {
            "title": title,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense Added")

    elif choice == "2":

        print(expenses)

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total =", total)

    elif choice == "4":

        break

    else:
        print("Invalid Choice")