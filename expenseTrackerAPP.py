from expenseTracker import ExpenseTracker
from employee import Employee
from department import Department
from expense import Expense
from typing import List

class ExpenseAPP:
    def __init__(self) -> None:
        self.expenseTracker = ExpenseTracker()

    def show_menue(self):
        print('\n=========================== Menu =====================================')
        print()
        print("1. Find/create/modify/delete employees.")
        print("2. Find/create/modify/delete departments.")
        print("3. Input employee's expense.")
        print("4. Generate monthly expense report for department.")
        print("5. Generate monthly summary expense category report for department.")
        print("6. Search monthly expenses for category.")
        print("7. Find employee with highest expense.")
        print("8. Find employee with lowest expense.")
        print("9. Find department over budgets.")
        print("10. Find department with highest expense.")
        print("11. Find department with lowest expense.")
        print("12. Give alerts to department close to exceeding budgets.")
        print("13. Display a histogram for expense category.")
        print("14. Display a histogram for departments' monthly expense.")
        print("15. Display a histogram for employees' monthly expense.")
        print("16. Modify the budget for category.")
        print("17. Modify all the expense category.")
        print("18. Exit")
        print('\n======================================================================\n')
        
    def get_choices(self):
        choice = int(input("Enter your choice: "))
        return choice
    
    def process_command(self, choice: int):
        if choice == 1:
            print('1. Find employee by employee ID.')
            print('2. Create new employee.')
            print('3. Modify employee.')
            print('4. Delete employee by employee ID.')
            print()
            input_num = int(input("Enter your choice: "))
            if input_num == 1:
                emp_id = int(input("Enter employee ID: \n"))
                self.expenseTracker.find_employee(emp_id)
            elif input_num == 2:
                emp_id = int(input("Enter employee ID: "))
                emp_fName = str(input("Enter employee first name: "))
                emp_lName = str(input("Enter employee last name: "))
                dept_id = int(input("Enter employee department ID: "))
                emp_dept_name = str(input("Enter employee department name: "))
                emp_rank = str(input("Enter employee rank: "))
                emp_expense = float(input("Enter employee expense: "))
                self.expenseTracker.add_employee(Employee(emp_id,emp_fName,emp_lName,dept_id,emp_dept_name,emp_rank,emp_expense))
                print("\nNew employee created.")
            elif input_num == 3:
                emp_id = int(input("Enter employee ID: "))
                emp_fName = str(input("Enter employee first name: "))
                emp_lName = str(input("Enter employee last name: "))
                dept_id = int(input("Enter employee department ID: "))
                emp_dept_name = str(input("Enter employee department name: "))
                emp_rank = str(input("Enter employee rank: "))
                emp_expense = str(input("Enter employee expense: "))
                self.expenseTracker.update_employee(Employee(emp_id,emp_fName,emp_lName,dept_id,emp_dept_name,emp_rank,emp_expense))
                print("\nEmployee updated.")
            elif input_num == 4:
                emp_id = int(input("Enter employee ID: "))
                self.expenseTracker.remove_employee(emp_id)
                print("\nEmployee deleted.")

        elif choice == 2:
            print('1. Find department by department ID.')
            print('2. Create new department.')
            print('3. Modify department.')
            print('4. Delete department by department ID.')
            print()
            input_num = int(input("Enter your choice: "))
            if input_num == 1:
                dept_id = int(input("Enter department ID: "))
                self.expenseTracker.find_department(dept_id)
            elif input_num == 2:
                dept_id = int(input("Enter department ID: "))
                dept_name = str(input("Enter department name: "))
                emp_id = int(input("Enter employee ID: "))
                emps = str(input("Enter employees: "))
                expense_category = str(input("Enter expense category: "))
                expense_month = int(input("Enter expense month: "))
                self.expenseTracker.add_department(Department(dept_id,dept_name,emp_id,emps,expense_category,expense_month))
                print("New department created.")
            elif input_num == 3:
                dept_id = int(input("Enter department ID: "))
                dept_name = str(input("Enter department name: "))
                emp_id = int(input("Enter employee ID: "))
                emps = str(input("Enter employees: "))
                expense_category = str(input("Enter expense category: "))
                expense_month = int(input("Enter expense month: "))
                self.expenseTracker.update_department(Department(dept_id,dept_name,emp_id,emps,expense_category,expense_month))
                print("Department updated.")
            elif input_num == 4:
                dept_id = int(input("Enter department ID: "))
                self.expenseTracker.remove_department(dept_id)
                print("Department deleted.")

        elif choice == 3:
            emp_id = int(input("Enter employee ID: "))
            date_of_expense = input("Enter date of expense:")
            expense_amount = float(input("Enter expense amount: "))
            expense_category = input("Enter employee's expense category: ")
            self.expenseTracker.input_employee_expense(Expense(emp_id,date_of_expense,expense_amount,expense_category))
            print("Employee's expense updated.")

        elif choice == 4:
            department_id = int(input("Enter department ID: "))
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.generate_monthly_expense_report(department_id, expense_month)

        elif choice == 5:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.generate_monthly_summary_report(expense_month)

        elif choice == 6:
            expense_month = int(input("Enter employee month: "))
            category = str(input("Enter category: "))
            self.expenseTracker.search_expense_by_category(expense_month, category)

        elif choice == 7:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.find_highest_expense_employee(expense_month)

        elif choice == 8:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.find_lowest_expense_employee(expense_month)

        elif choice == 9:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.find_department_over_budget(expense_month)
            
        elif choice == 10:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.find_highest_expense_department(expense_month)

        elif choice == 11:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.find_lowest_expense_department(expense_month)

        elif choice == 12:
            expense_month = int(input("Enter employee month: "))
            budget_limit_percentage = int(input("Enter budget limit percentage: "))
            self.expenseTracker.give_alerts_to_departments(expense_month, budget_limit_percentage)

        elif choice == 13:
            dept_id = int(input("Enter department ID: "))
            expense_month = int(input("Enter expense month: "))
            self.expenseTracker.display_histogram_for_total_count_of_departments(dept_id, expense_month)

        elif choice == 14:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.display_histogram_for_monthly_expense_of_department(expense_month)

        elif choice == 15:
            expense_month = int(input("Enter employee month: "))
            self.expenseTracker.display_histogram_for_monthly_expense_of_employees(expense_month)

        elif choice == 16:
            category_name = str(input("Enter category name: "))
            reduce_percentage = int(input("Enter reduce percentage: "))
            self.expenseTracker.modify_budget_for_given_category(category_name, reduce_percentage)

        elif choice == 17:
            reduce_percentage = int(input("Enter reduce percentage: "))
            self.expenseTracker.reduce_budget_for_all_category(reduce_percentage)

        elif choice == 18:
            return 

        else:
            print('Invalid choice! ')

def main():
    app = ExpenseAPP()
    while True:
        app.show_menue()
        choice = app.get_choices()
        if choice == 18: 
            print("Bye! ")
            break
        app.process_command(choice)

if __name__ == "__main__":
    main()