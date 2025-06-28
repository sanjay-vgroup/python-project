
print("Welcome to Expense Tracker Application")
print("Track your daily and monthly expense on day to day basis and save them for future reference.")


def add_expense(expense):
    # Function to add expense
    
    date = input("Enter the date of expense (YYYY-MM-DD): ")
    category = input("Enter the category of the expense (e.g., Food, Transport, etc.): ")
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description of the expense: ")
    expense.append({
        "date": date,
        "amount": amount,
        "description": description,
        "category": category
    }) 
    print("Expense added successfully!")

def view_expense(expense):
    # Function to view all expenses
    if not expense:
        print("No expenses recorded.")
        return
    for i, exp in enumerate(expense, start=1):
        print(f"{i}. Date: {exp['date']}, Amount: ${exp['amount']:.2f}, Description: {exp['description']}, Category: {exp['category']}")    

def track_budget(expense):
#check expsense object is not empty
    if not expense:
        print("No expenses recorded to track budget.")
        return  
    # Function to track budget  
    print("Tracking your budget...")

    # get budget from user
    budget = float(input("Enter your monthly budget: "))
    # calculate total expenses
    total_expense = sum(exp['amount'] for exp in expense)
    # check if total expenses exceed budget
    if total_expense > budget:
        print(f"Warning: You have exceeded your budget by ${total_expense - budget:.2f}.")      
    else:  
        print(f"You are within your budget. Total expenses: ${total_expense:.2f}, Budget: ${budget:.2f}.")  

#save expense function will save expense to a file
def save_expense(expense):
    # Function to save expenses to a file
    with open('expenses.txt', 'w') as file:
        for exp in expense:
            file.write(f"{exp['date']},{exp['amount']},{exp['description']},{exp['category']}\n")
    print("Expenses saved successfully!")

# load expense function will load expense from a file
def load_expense(): 
    # Function to load expenses from a file
    expense = []
    try:
        with open('expenses.txt', 'r') as file:
            for line in file:
                date, amount, description, category = line.strip().split(',')
                expense.append({
                    "date": date,
                    "amount": float(amount),
                    "description": description,
                    "category": category
                })
        print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No saved expenses found.")
    return expense

def save_expense(expense):
    # Function to save expenses to a file
    with open('expenses.txt', 'w') as file:
        for exp in expense:
            file.write(f"{exp['date']},{exp['amount']},{exp['description']},{exp['category']}\n")
    print("Expenses saved successfully!")

#calling menu function to print menu items
def menu():
    print("==================================")
    print("Menu Items")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Track Budget")
    print("4. Save Expense")
    print("5. Exit")    

def main():
    expense = []
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_expense(expense)
        elif choice == '2':
            view_expense(expense)
        elif choice == '3':
            track_budget(expense)
        elif choice == '4':
            save_expense(expense)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
# This is the main entry point of the application
