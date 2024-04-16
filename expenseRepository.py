from expense import Expense
import csv
from typing import List
 
class ExpenseRepository:
    def __init__(self, filename: str = "expense.csv") -> None:
        self.__filename = filename

    def read_expenses(self) -> List[Expense]:
        expenses: List[Expense] = []

        with open(self.__filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4: continue
                expense = Expense(int(row[0]), row[1], float(row[2]), row[3])
                expenses.append(expense)
        return expenses

    def write_expenses(self, expenses: List[Expense]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for expense in expenses:
                writer.writerow(expense.get_csv())

    def update_expense(self, new_expense: Expense) -> None:
        expenses = self.read_expenses()
        found = False
        for i, expense in enumerate(expenses):
            if expense.employee_id == new_expense.employee_id:
                expenses[i] = new_expense
                found = True
                break
        if found:
            self.write_expenses(expenses)
        else:
            raise ValueError("Expense not found.")


    def delete_expense(self, employee_id: int) -> None:
        expenses = self.read_expenses()
        found = False
        for i, expense in enumerate(expenses):
            if expense.employee_id == employee_id:
                del expenses[i]
                found = True
                break
        if found:
            self.write_expenses(expenses)
        else:
            raise ValueError("Expense not found.")

def main():
    db = ExpenseRepository()
    expenses = db.read_expenses()
    for expense in expenses:
        print(expense)
    print()

    new_expense = Expense(1222, '3-1-2023', 600.0, 'Membership fees')
    expenses.append(new_expense)
    db.write_expenses(expenses)

    modified_expense = Expense(1222, '3-22-2023', 888.0, 'Training')
    db.update_expense(modified_expense)

    db.delete_expense(1222)

    expenses = db.read_expenses()
    for expense in expenses:
        print(expense)

if __name__ == "__main__":
    main()