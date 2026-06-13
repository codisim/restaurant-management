
from abc import ABC


class User(ABC):
    def __init__(self, name, email, phobe, address):
        self.name = name
        self.email = email
        self.phobe = phobe
        self.address = address




class Employee(User):
    def __init__(self, name, email, phone, address, age, dasignation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.dasignation = dasignation
        self.salary = salary



# emp = Employee("Rahim", "rahim@example.com", "1234567890", "123 Main St", 30, "Manager", 50000)
# print(emp.name)




class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)


    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)
        

    

    def view_employees(self):
        print("List of Employees:")
        for employee in self.employees:
            print(f"Name: {employee.name}, Email: {employee.email}, Phone: {employee.phobe}, Address: {employee.address}, Age: {employee.age}, Designation: {employee.dasignation}, Salary: {employee.salary}")





class Restaurant():
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee) 





ad = Admin("Admin", "admin@example.com", "0987654321", "456 Admin St")
restaurant = Restaurant("My Restaurant")
ad.add_employee(restaurant, Employee("Rahim", "rahim@example.com", "1234567890", "123 Main St", 30, "Manager", 50000))
ad.add_employee(restaurant, Employee("Karim", "karim@example.com", "0987654321", "456 Main St", 25, "Developer", 40000))
ad.add_employee(restaurant, Employee("Jamal", "jamal@example.com", "1111111111", "789 Main St", 28, "Designer", 45000))
ad.view_employees()







