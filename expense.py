from typing import List

class Expense:
    def __init__(self, employee_id: int, date_of_expense: str, expense_amount: float, expense_category: str) -> None:
        self.__employee_id = employee_id
        self.__date_of_expense = date_of_expense
        self.__expense_amount = expense_amount
        self.__expense_category = expense_category
    
    @property
    def employee_id(self) -> int:
        return self.__employee_id
    
    @property
    def date_of_expense(self) -> str:
        return self.__date_of_expense
    
    @property
    def expense_amount(self) -> float:
        return self.__expense_amount
    
    @property
    def expense_category(self) -> float:
        return self.__expense_category

    def __str__(self) -> str:
        return f"Employee ID: {self.__employee_id}, Date of expense: {self.__date_of_expense}, Expense amount: {self.__expense_amount}, Expense category: {self.__expense_category}"
    
    def get_csv(self) -> List[str]:
        csv_str: List[str] = [int(self.__employee_id), str(self.__date_of_expense), float(self.__expense_amount), str(self.__expense_category)]
        return csv_str

    def __eq__(self, __o: object) -> bool:
        if isinstance( __o, Expense):
            return __o.__employee_id == self.__employee_id
        else:
            return False