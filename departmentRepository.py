import csv
from department import Department, Budget
from typing import List

class DepartmentRepository:
    def __init__(self, file_department: str = "department.csv", file_monthly_budget: str = "monthly_budget.csv") -> None:
        self.__file_department = file_department
        self.__file_monthly_budget = file_monthly_budget

    def read_departments(self) -> List[Department]:
        departments: List[Department] = []

        with open(self.__file_department, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 6:continue
                # department_id = int(row[0])
                # department_name = row[1]
                # expense_month = int(row[2])
                # manager_name = row[3]
                # expense_categories = list(row[4]).split(',')
                # expense_month = int(row[5])
                # department = Department(department_id, department_name, expense_month, manager_name, expense_categories, expense_month)
                department = Department(int(row[0]), row[1], int(row[2]), row[3], row[4], int(row[5]))
                departments.append(department)
        return departments

    def write_departments(self, departments: List[Department]) -> None:
        with open(self.__file_department, "w", newline="") as file:
            writer = csv.writer(file)
            for department in departments:
                writer.writerow(department.get_csv())

    def update_department(self, department_id: int, new_department: Department) -> None:
        departments = self.read_departments()
        found = False
        for i, department in enumerate(departments):
            if department.department_id == department_id:
                departments[i] = new_department
                found = True
                break
        if found:
            self.write_departments(departments)
        else:
            raise ValueError("Department not found.")

    def delete_department(self, department_id: int) -> None:
        departments = self.read_departments()
        found = False
        for i, department in enumerate(departments):
            if department.department_id == department_id:
                del departments[i]
                found = True
                break
        if found:
            self.write_departments(departments)
        else:
            raise ValueError("Department not found.")
        
    def read_monthly_budget(self):
        monthly_budgets: List[Budget]  = []

        with open(self.__file_monthly_budget, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 4: continue
                monthly_budget = Budget(row[0], row[1], float(row[2]), int(row[3]))
                monthly_budgets.append(monthly_budget)
        return monthly_budgets
    
    def write_monthly_budget(self, monthly_budgets: List[Budget]) -> None:
        with open(self.__file_monthly_budget, "w", newline="") as file:
            writer = csv.writer(file)
            for monthly_budget in monthly_budgets:
                writer.writerow(monthly_budget.get_csv())
    
    def update_monthly_budget(self, new_budget: Budget) -> None:
        monthly_budgets = self.read_monthly_budget()
        found = False
        for i, monthly_budget in enumerate(monthly_budgets):
            if monthly_budget.department_name == new_budget.department_name and monthly_budget.budget_month == new_budget.budget_month:
                monthly_budgets[i] = new_budget
                found = True
                break
        if found:
            self.write_monthly_budget(monthly_budgets)
        else:
            raise ValueError("Monthly_budgets not found.")
        
    def delete_monthly_budget(self, department_name: str, expense_category: str) -> None:
        monthly_budgets = self.read_monthly_budget()
        found = False
        for i, monthly_budget in enumerate(monthly_budgets):
            if monthly_budget.department_name == department_name and monthly_budget.expense_category == expense_category:
                del monthly_budgets[i]
                found = True
                break
        if found:
            self.write_monthly_budget(monthly_budgets)
        else:
            raise ValueError("Monthly_budgets not found.")

def main():
    db = DepartmentRepository()
    departments = db.read_departments()
    for department in departments:
        print(department)
    print()

    new_department = Department(666, 'HR', 1817, 'John Smith', "Training',40000.0", 2)
    departments.append(new_department)
    db.write_departments(departments)

    modified_department = Department(666, 'HR', 1817, 'John Doe', "Training',5300.0", 2)
    db.update_department(666, modified_department)

    # db.delete_department(666)

    departments = db.read_departments()
    for department in departments:
        print(department)

    # print("****************************************************")

    # monthly_budgets = db.read_monthly_budget()
    # for monthly_budget in monthly_budgets:
    #     print(monthly_budget)
    # print()

    # new_budget = Budget('Marketing','Transportation', 4500.0, 2)
    # monthly_budgets.append(new_budget)
    # db.write_monthly_budget(monthly_budgets)

    # modified_dept_engineering = Budget('Marketing','Transportation',5300.0, 2)
    # db.update_monthly_budget(modified_dept_engineering)

    # db.delete_monthly_budget('Marketing','Transportation')

    # monthly_budgets = db.read_monthly_budget()
    # for monthly_budget in monthly_budgets:
    #     print(monthly_budget)

if __name__ == "__main__":
    main()

