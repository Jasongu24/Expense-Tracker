# Expense Tracker README

## Introduction
Expense Tracker is a software application designed for the CFO of a high-tech company to monitor and manage employee spending efficiently. It enables tracking expenses by employee, department, and category, facilitating better budget planning and control.

## Data Details
Expense Tracker requires the following data fields:
- **Employee Information**: Employee ID, First Name, Last Name, Department Name, Rank.
- **Expense Records**: Date of Expense, Expense Amount, Expense Category, Employee ID.
- **Department Details**: Department Name, List of Employees, List of Expense Categories with Budgets.

## Storage
Expense data is stored in individual files for each employee's expenses. Monthly budgets for expense categories are stored in a separate file, organized by department.

## Core Functionalities
Expense Tracker provides essential functionalities including:
- Employee and department record management.
- Input of employee expenses.
- Generation of monthly expense reports for departments and months.
- Monthly summary reports for each expense category in each department.
- Search functionality for monthly expenses by category.
- Identification of highest spending employees and departments.
- Alerts for departments nearing budget limits.
- Histograms for expense categories and department expenses.

## User Interface
Expense Tracker features a console-based user interface with clear guidance, data validation, and error handling.

## OOD Process
1. **Understand requirements**: Use Case Diagrams.
2. **Design business objects**: Identify data attributes, classes, and methods.
3. **Follow Object-oriented design principles**: Encapsulation, loose coupling, design patterns.
4. **Implement and test**: Business objects, presentation layer, data layer.

## License
This project is licensed under the [MIT License](LICENSE).
