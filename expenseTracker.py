from departmentRepository import DepartmentRepository
from employeeRepository import EmployeeRepository
from expenseRepository import ExpenseRepository
from employee import Employee
from department import Department
from expense import Expense
from typing import List
from collections import defaultdict
# import matplotlib.pyplot as plt
import collections

class ExpenseTracker:
    def __init__(self) -> None:
        self.__departments = DepartmentRepository().read_departments()
        self.__budgets = DepartmentRepository().read_monthly_budget()
        self.__employees = EmployeeRepository().read_employees()
        self.__expenses = ExpenseRepository().read_expenses()
        self.__emp_repository = EmployeeRepository()
        self.__dept_repository = DepartmentRepository()
        self.__expense_repository = ExpenseRepository()
    
    def find_employee(self, employee_id: int) -> None:
        for emp in self.__employees:
            if emp.employee_id == employee_id:
                print(emp) 
        return None
    
    def add_employee(self, employee: Employee) -> None:
        if employee not in self.__employees:
            self.__employees.append(employee)
            self.__emp_repository.write_employees(self.__employees)

    def update_employee(self, new_employee: Employee) -> None:
        self.__emp_repository.update_employee(new_employee)

    def remove_employee(self, employee_id: int) -> None:
        self.__emp_repository.delete_employee(employee_id)
    
    def find_department(self, department_id: int) -> None:
        for dept in self.__departments:
            if dept.department_id == department_id:
                print(dept)
        return None
    
    def add_department(self, department: Department) -> None:
        if department not in self.__departments:
            self.__departments.append(department)
            self.__dept_repository.write_departments(self.__departments)

    def update_department(self, new_department: Department) -> None:
        self.__dept_repository.update_department(new_department.department_id, new_department)

    def remove_department(self, department_id: int) -> None:
        self.__dept_repository.delete_department(department_id)
    
    def input_employee_expense(self, new_expense: Expense):
        self.__expense_repository.update_expense(new_expense)

    def generate_monthly_expense_report(self, department_id: int, expense_month: int) -> None:
        for dept in self.__departments:
            if dept.department_id == department_id and dept.expense_month == expense_month:
                print(dept)
        return None 

    def generate_monthly_summary_report(self, expense_month: int) -> List[str]:
        department_budgets = defaultdict(float)
        for dept in self.__departments:
            if dept.expense_month == expense_month:
                department_id = dept.department_id
                expense_category = dept.expense_categories.split("', '")[0]
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                department_budgets[(department_id, expense_category)] += budget

        for (department_id, expense_category), budget_sum in department_budgets.items():
            department_name = None
            for dept in self.__departments:
                if dept.department_id == department_id and dept.expense_categories.split("', '")[0] == expense_category:
                    department_name = dept.department_name
                    break
            if department_name is not None:
                print(f"Department: {department_name} has expense category: {expense_category} with budgets: ${budget_sum} in month: {expense_month}.")

    def search_expense_by_category(self, expense_month: int, search_category: str) -> None:
        department_budgets = defaultdict(float)
        for dept in self.__departments:
            if dept.expense_month == expense_month and dept.expense_categories.split("', '")[0] == search_category:
                department_id = dept.department_id
                expense_category = dept.expense_categories.split("', '")[0]
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                department_budgets[(department_id, expense_category)] += budget

        for (department_id, expense_category), budget_sum in department_budgets.items():
            department_name = None
            for dept in self.__departments:
                if dept.department_id == department_id and dept.expense_categories.split("', '")[0] == expense_category:
                    department_name = dept.department_name
                    break
            if department_name is not None:
                print(f"Department: {department_name} has expense category: {expense_category} with budgets: ${budget_sum} in month: {expense_month}.")

    def find_highest_expense_employee(self, expense_month: int) -> str:
        max_expense = float('-inf')
        employee_name = ""
        for dept in self.__departments:
            if dept.expense_month == expense_month:
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                if budget > max_expense:
                    max_expense = budget
                    employee_name = dept.employees
        if employee_name:
            print(f"The employee with the highest expense in month {expense_month} is: {employee_name} with a budget of ${max_expense}.")

    def find_lowest_expense_employee(self, expense_month: int) -> str:
        min_expense = float('inf')
        employee_name = ""
        for dept in self.__departments:
            if dept.expense_month == expense_month:
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                if budget < min_expense:
                    min_expense = budget
                    employee_name = dept.employees
        if employee_name:
            print(f"The employee with the lowest expense in month {expense_month} is: {employee_name} with a budget of ${min_expense}.")

    def find_department_over_budget(self, expense_month: int) -> None:
        department_budgets = defaultdict(float)
        departments_over_budget = []
        budget_limit = {}

        for dept in self.__departments:
            if dept.expense_month == expense_month:
                department_name = dept.department_name
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                department_budgets[department_name] += budget

        for dept in self.__budgets:
            if dept.department_name not in budget_limit:
                budget_limit[dept.department_name] = 0
            budget_limit[dept.department_name] += dept.budget_limit

        for department_name, budget_sum in department_budgets.items():
            if department_name in budget_limit and budget_sum > budget_limit[department_name]:
                departments_over_budget.append(department_name)
            print(f"Department: {department_name} with expenses: {budget_sum} over budget limit: {budget_limit[department_name]}")

    def find_highest_expense_department(self, expense_month: int) -> None:
        max_expense = float('-inf')
        department_name = ""
        for dept in self.__departments:
            if dept.expense_month == expense_month:
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                if budget > max_expense:
                    max_expense = budget
                    department_name = dept.department_name
        if department_name:
            print(f"The department with the highest expense in month {expense_month} is: {department_name} with a budget of ${max_expense}.")
    
    def find_lowest_expense_department(self, expense_month: int) -> None:
        min_expense = float('inf')
        department_name = ""
        for dept in self.__departments:
            if dept.expense_month == expense_month:
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                if budget < min_expense:
                    min_expense = budget
                    department_name = dept.department_name
        if department_name:
            print(f"The department with the lowest expense in month {expense_month} is: {department_name} with a budget of ${min_expense}.")  

    def give_alerts_to_departments(self, expense_month: int, threshold_percent: float) -> None:
        department_budgets = defaultdict(float)
        budget_limit = {}

        for dept in self.__departments:
            if dept.expense_month == expense_month:
                department_name = dept.department_name
                budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                department_budgets[department_name] += budget

        for dept in self.__budgets:
            if dept.department_name not in budget_limit:
                budget_limit[dept.department_name] = 0
            budget_limit[dept.department_name] += dept.budget_limit

        for department_name, budget_sum in department_budgets.items():
            if department_name in budget_limit:
                budget_limit_for_dept = budget_limit[department_name]
                remaining_budget = budget_limit_for_dept - budget_sum
                threshold_amount = budget_limit_for_dept * (threshold_percent / 100)
                if remaining_budget <= threshold_amount:
                    print(f"ALERT: Department {department_name} is close to exceeding its budget limit for the month {expense_month}.")

    def display_histogram_for_total_count_of_departments(self, department_id: int, expense_month: int) -> None:
        expenses_by_category = {}
        for dept in self.__departments:
            if dept.department_id == department_id and dept.expense_month == expense_month:
                for category, expense in dept.expense_categories.items():
                    if category not in expenses_by_category:
                        expenses_by_category[category] = 0
                    expenses_by_category[category] += expense
        # plt.bar(range(len(expenses_by_category)), list(expenses_by_category.values()), align='center')
        # plt.xticks(range(len(expenses_by_category)), list(expenses_by_category.keys()))
        # plt.title(f"Expense category counts for Department {department_id} - Month {expense_month}")
        # plt.show()

    def display_histogram_for_monthly_expense_of_department(self, expense_month: int) -> None:
        expenses_by_department = {}
        for dept in self.__departments:
            if dept.expense_month == expense_month:
                if dept.department_name not in expenses_by_department:
                    expenses_by_department[dept.department_name] = 0
                for expense in dept.expense_categories.values():
                    expenses_by_department[dept.department_name] += expense
        # plt.bar(range(len(expenses_by_department)), list(expenses_by_department.values()), align='center')
        # plt.xticks(range(len(expenses_by_department)), list(expenses_by_department.keys()))
        # plt.title(f"Department expenses for Month {expense_month}")
        # plt.show()

    def display_histogram_for_monthly_expense_of_employees(self, expense_month: int) -> None:
        expenses_by_employee = {}
        for dept in self.__departments:
            if dept.expense_month == expense_month:
                for employee_id, expense in dept.employees.items():
                    if employee_id not in expenses_by_employee:
                        expenses_by_employee[employee_id] = 0
                    expenses_by_employee[employee_id] += sum(expense.values())
        # plt.bar(range(len(expenses_by_employee)), list(expenses_by_employee.values()), align='center')
        # plt.xticks(range(len(expenses_by_employee)), list(expenses_by_employee.keys()))
        # plt.title(f"Employee expenses for Month {expense_month}")
        # plt.show()

    def modify_budget_for_given_category(self, category: str, percent_reduction: float) -> None:
        for dept in self.__departments:
            expense_category = dept.expense_categories.split("', '")[0]
            if expense_category == category:
                prev_budget = float(dept.expense_categories.split("', '")[1].replace(',', ''))
                prev_expense_categories = dept.expense_categories
                new_budget = prev_budget *  (1 - percent_reduction / 100) 
                dept.expense_categories = f"'{expense_category}', '{new_budget}'"
                print(f"Modified expense category: {expense_category}'s original budget: {prev_budget} to new budget: {new_budget}")

    def reduce_budget_for_all_category(self, percent_reduction: float) -> None:
        for dept in self.__departments:
            expense_categories = dept.expense_categories.split("', '")
            if len(expense_categories) >= 2:
                expense_category = expense_categories[0].replace("'", "")
                prev_budget = float(expense_categories[1].replace(',', ''))
                new_budget = prev_budget * (1 - percent_reduction / 100)
                dept.expense_categories = f"'{expense_category}', '{new_budget}'"
                print(f"Modified expense category: {expense_category}'s original budget: {prev_budget} to new budget: {new_budget}")

def main():
    et = ExpenseTracker()
    er = EmployeeRepository()
    dr = DepartmentRepository()
    exr = ExpenseRepository()

    et.find_employee(1215)
    et.add_employee(Employee(1218, 'Rachel', 'Brown', 111, 'Engineering', 'Supervisor', 2000.0))
    et.update_employee(Employee(1218, 'Rachel', 'Brown', 222, 'Marketing', 'Supervisor', 2500.0))
    et.remove_employee(1218)
    employees = er.read_employees()
    for employee in employees:
        print(employee)
    print()

    et.find_department(222)
    et.add_department(Department(666, 'HR', 1817, 'John Smith', "Training',40000.0", 2))
    et.update_department(Department(666, 'HR', 1817, 'John Doe', "Training',5300.0", 2))
    et.remove_department(666)
    departments = dr.read_departments()
    for department in departments:
        print(department)
    print()
    
    et.input_employee_expense(Expense(1222, '3-1-2023', 600.0, 'Membership fees'))
    expenses = exr.read_expenses()
    for expense in expenses:
        print(expense)
    print()

    et.generate_monthly_expense_report(111,3)
    et.generate_monthly_summary_report(3)
    et.search_expense_by_category(3,'Training')
    et.find_highest_expense_employee(3)
    et.find_lowest_expense_employee(3)
    et.find_department_over_budget(3)
    et.find_highest_expense_department(3)
    et.find_lowest_expense_department(3)
    et.give_alerts_to_departments(3,90)
    et.display_histogram_for_total_count_of_departments(111,3)
    et.display_histogram_for_monthly_expense_of_department(3)
    et.display_histogram_for_monthly_expense_of_employees(3)
    et.modify_budget_for_given_category('Training',10)
    et.reduce_budget_for_all_category(10)

if __name__ == "__main__":
    main()