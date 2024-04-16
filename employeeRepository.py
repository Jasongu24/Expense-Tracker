from employee import Employee
import csv
from typing import List


class EmployeeRepository:
    def __init__(self, filename: str = "employees.csv") -> None:
        self.__filename = filename

    def read_employees(self) -> List[Employee]:
        employees: List[Employee] = []

        with open(self.__filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 7: continue
                employee = Employee(int(row[0]), row[1], row[2], int(row[3]), row[4], row[5],float(row[6]))
                employees.append(employee)
        return employees

    def write_employees(self, employees: List[Employee]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            for employee in employees:
                writer.writerow(employee.get_csv())

    def update_employee(self, new_employee: List[Employee]) -> None:
        employees = self.read_employees()
        found = False
        for i, employee in enumerate(employees):
            if employee.employee_id == new_employee.employee_id:
                employees[i] = new_employee
                found = True
                break
        if found:
            self.write_employees(employees)
        else:
            raise ValueError("Employee not found.")

    def delete_employee(self, employee_id: int) -> None:
        employees = self.read_employees()
        found = False
        for i, employee in enumerate(employees):
            if employee.employee_id == employee_id:
                del employees[i]
                found = True
                break
        if found:
            self.write_employees(employees)
        else:
            raise ValueError("Employee not found.")

def main():
    db = EmployeeRepository()
    employees = db.read_employees()
    for employee in employees:
        print(employee)
    print()

    new_employee = Employee(1218, 'Rachel', 'Brown', 111, 'Engineering', 'Supervisor', 2000.0)
    employees.append(new_employee)
    db.write_employees(employees)

    modified_employee = Employee(1218, 'Rachel', 'Brown', 222, 'Marketing', 'Supervisor', 2500.0)
    db.update_employee(modified_employee)

    db.delete_employee(1218)

    employees = db.read_employees()
    for employee in employees:
        print(employee)

if __name__ == "__main__":
    main()
