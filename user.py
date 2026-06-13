
from abc import ABC


# User class to represent a user of the restaurant system
class User(ABC):
    def __init__(self, name, email, phobe, address):
        self.name = name
        self.email = email
        self.phobe = phobe
        self.address = address



# Employee class to represent an employee of the restaurant
class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary



# emp = Employee("Rahim", "rahim@example.com", "1234567890", "123 Main St", 30, "Manager", 50000)
# print(emp.name)



# Admin class to manage employees
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)


    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)


    def view_employees(self, restaurant):
        restaurant.view_employees()
        
    




# Restaurant class to manage employees
class Restaurant():
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee) 


    def view_employees(self):
        print("List of Employees:")
        for employee in self.employees:
            print(f"Name: {employee.name}, Email: {employee.email}, Phone: {employee.phobe}, Address: {employee.address}, Age: {employee.age}, Designation: {employee.dasignation}, Salary: {employee.salary}")



# Menu class to represent a menu item
class Menu():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"Item '{item_name}' removed from the menu.")
        else:
            print(f"Item '{item_name}' not found in the menu.")
            
            
    def view_menu(self):
        print("Menu Items:")
        for item in self.items:
            print(f"Name: {item.name}, Price: {item.price}, Description: {item.description}")





























ad = Admin("Admin", "admin@example.com", "0987654321", "456 Admin St")
restaurant = Restaurant("My Restaurant")
ad.add_employee(restaurant, Employee("Rahim", "rahim@example.com", "1234567890", "123 Main St", 30, "Manager", 50000))
ad.add_employee(restaurant, Employee("Karim", "karim@example.com", "0987654321", "456 Main St", 25, "Developer", 40000))
ad.add_employee(restaurant, Employee("Jamal", "jamal@example.com", "1111111111", "789 Main St", 28, "Designer", 45000))
ad.view_employees()







