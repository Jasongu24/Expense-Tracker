from typing import  List

class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, department_id: int, department_name: str, rank: str, expense: float) -> None:
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__department_id = department_id
        self.__department_name = department_name
        self.__rank = rank
        self.__expense = expense
    
    @property
    def employee_id(self) -> int:
        return self.__employee_id
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def department_id(self) -> str:
        return self.__department_id
    
    @property
    def department_name(self) -> str:
        return self.__department_name
    
    @property
    def rank(self) -> str:
        return self.__rank
    
    @property
    def expense(self) -> str:
        return self.__expense

    def __str__(self) -> str:
        return f"Employee ID: {self.__employee_id}, First name: {self.__first_name}, Last name: {self.__last_name}, Department ID: {self.__department_id}, Department name: {self.__department_name}, Rank: {self.__rank}, Expense: {self.__expense}"
    
    def get_csv(self) -> List[str]:
        csv_str: List[str] = [int(self.__employee_id), str(self.__first_name), str(self.__last_name), int(self.__department_id), str(self.__department_name), str(self.__rank), float(self.__expense)]
        return csv_str

    def __eq__(self, __o: object) -> bool:
        if isinstance( __o, Employee):
            return __o.__employee_id == self.__employee_id
        else:
            return False