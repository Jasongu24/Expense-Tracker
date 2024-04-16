from typing import List

class Department:
    def __init__(self, department_id: int, department_name: str, employee_id: int, employees: str, expense_categories: str, expense_month: int) -> None:
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
    def employees(self) -> str:
        return self.__employees
    
    @property
    def expense_categories(self) -> list:
        return self.__expense_categories
    
    @expense_categories.setter
    def expense_categories(self, expense_categories: str) -> None:
        self.prev_expense_categories = self.__expense_categories 
        self.__expense_categories = expense_categories
    
    @property
    def expense_month(self) -> float:
        return self.__expense_month

    def __str__(self) -> str:
        return f"Department ID: {self.__department_id}, Department name: {self.__department_name}, Employee ID: {self.__employee_id}, Employees: {self.__employees}, Expense categories: {self.__expense_categories}, Expense month: {self.__expense_month}"
    
    def get_csv(self) -> List[str]:
        csv_str: List[str] = [int(self.__department_id), str(self.__department_name), int(self.__employee_id), str(self.__employees), str(self.__expense_categories), int(self.__expense_month)]
        return csv_str

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Department):
            return other.__department_id == self.__department_id
        else:
            return False

class Budget:
    def __init__(self, department_name: str, expense_category: str, budget_limit: float, budget_month: int) -> None:
        self.__department_name = department_name
        self.__expense_category = expense_category
        self.__budget_limit = budget_limit
        self.__budget_month = budget_month

    @property
    def department_name(self) -> int:
        return self.__department_name
    
    @property
    def expense_category(self) -> int:
        return self.__expense_category
    
    @property
    def budget_limit(self) -> float:
        return self.__budget_limit
    
    @property
    def budget_month(self) -> float:
        return self.__budget_month
    
    def __str__(self) -> str:
        return f"Department name: {self.__department_name}, Expense category: {self.__expense_category}, Budget limits: {self.__budget_limit}, Budget month: {self.__budget_month}"
    
    def get_csv(self) -> List[str]:
        csv_str: List[str] = [self.__department_name, self.__expense_category, float(self.__budget_limit), int(self.__budget_month)]
        return csv_str

    def __eq__(self, __o: object) -> bool:
        if isinstance( __o, Budget):
            return (__o.__department_name == self.__department_name) and (__o.__expense_category == self.__expense_category)
        else:
            return False
 