from menu import Menu


# Restaurant class to manage employees
class Restaurant():
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee) 


    def view_employees(self):
        print("List of Employees:")
        print("Name\tEmail\tPhone\tAddress\tAge\tDesignation\tSalary")
        for employee in self.employees:
            print(f"{employee.name}\t{employee.email}\t{employee.phobe}\t{employee.address}\t{employee.age}\t{employee.designation}\t{employee.salary}")
            
            

