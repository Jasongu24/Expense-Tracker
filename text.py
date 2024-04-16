from departmentRepository import DepartmentRepository
from employeeRepository import EmployeeRepository
from expenseRepository import ExpenseRepository
from employee import Employee
from department import Department
import csv
from typing import List

class ExpenseTracker:
    def __init__(self) -> None:
        self.__departments = DepartmentRepository().read_departments()
        
    def find_department(self, department_id: int) -> None:
        for dept in self.__departments:
            if dept.department_id == department_id:
                print(dept) 
        return None
    
    def add_department(self, department: Department) -> None:
        dept_repository = DepartmentRepository()
        if department not in self.__departments:
            self.__departments.append(department)
            dept_repository.write_departments(self.__departments)

    def update_department(self, new_department: Department) -> None:
        dept_repository = DepartmentRepository()
        for i, dept in enumerate(self.__departments):
            if dept.department_id == new_department.department_id:
                self.__departments[i] = new_department
                dept_repository.update_department(new_department)

    def remove_department(self, department_id: int) -> None:
        dept_repository = DepartmentRepository()
        for i, dept in enumerate(self.__departments):
            if dept.department_id == department_id:
                self.__departments.pop(i)
                dept_repository.delete_department(department_id)

class Department:
    def __init__(self, department_id: int, department_name: str, employee_id: int, employees: list, expense_categories: dict, expense_month: int) -> None:
        self.__department_id = department_id
        self.__department_name = department_name
        self.__employee_id = employee_id
        self.__employees = employees
        self.__expense_categories = expense_categories
        self.__expense_month = expense_month
    
    @property
    def department_id(self) -> int:
        return self.__department_id
    
    @property
    def department_name(self) -> str:
        return self.__department_name
     
    @property
    def employee_id(self) -> int:
        return self.__employee_id
    
    @property
    def employees(self) -> list:
        return self.__employees
    
    @property
    def expense_categories(self) -> dict:
        return self.__expense_categories
    
    @property
    def expense_month(self) -> float:
        return self.__expense_month

    def __str__(self) -> str:
        return f"Department ID: {self.__department_id}, Department name: {self.__department_name}, Employee ID: {self.__employee_id}, Employees: {self.__employees}, Expense categories: {self.__expense_categories}, Expense month: {self.__expense_month}"
    
    def get_csv(self) -> List[str]:
        csv_str: List[str] = str[int(self.__department_id), str(self.__department_name), int(self.__employee_id), str(self.__employees), dict(self.__expense_categories), int(self.__expense_month)]
        return csv_str

class DepartmentRepository:
    def __init__(self, file_department: str = "department.csv", file_monthly_budget: str = "monthly_budget.csv") -> None:
        self.__file_department = file_department
        self.__file_monthly_budget = file_monthly_budget

    def read_departments(self):
        departments: List[Department]  = []

        with open(self.__file_department, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 6: continue
                department = Department(int(row[0]), row[1], int(row[2]), row[3], dict(row[4]), int(row[5]))
                departments.append(department)
        return departments

    def write_departments(self, departments: List[Department]) -> None:
        with open(self.__file_department, "w", newline="") as file:
            writer = csv.writer(file)
            for department in departments:
                writer.writerow(department.get_csv())

    def update_department(self, new_department: List[Department]) -> None:
        departments = self.read_departments()
        found = False
        for i, department in enumerate(departments):
            if department.department_id == new_department.department_id and department.employee_id == new_department.employee_id:
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

def main():
    ex = ExpenseTracker()
    ex.find_department(111)

if __name__ == "__main__":
    main()
