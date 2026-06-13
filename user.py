
from abc import ABC


# User class to represent a user of the restaurant system
class User(ABC):
    def __init__(self, name, email, phobe, address):
        self.name = name
        self.email = email
        self.phobe = phobe
        self.address = address



class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.card = Node
        
    def view_menu(self, restaurant):
        restaurant.menu.view_menu()


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
        
    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_item(item)
        
    def remove_menu_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)
        
    




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
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
            
    
    

class MenuItem():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    
    
    
    
    
mn = Menu()
item1 = MenuItem("Pizza", 10.99, 20)
item2 = MenuItem("Burger", 5.99, 30)
item3 = MenuItem("Pasta", 8.99, 25)
mn.add_item(item1)
mn.add_item(item2)
mn.add_item(item3)
mn.view_menu()





























# ad = Admin("Admin", "admin@example.com", "0987654321", "456 Admin St")
# restaurant = Restaurant("My Restaurant")
# ad.add_employee(restaurant, Employee("Rahim", "rahim@example.com", "1234567890", "123 Main St", 30, "Manager", 50000))
# ad.add_employee(restaurant, Employee("Karim", "karim@example.com", "0987654321", "456 Main St", 25, "Developer", 40000))
# ad.add_employee(restaurant, Employee("Jamal", "jamal@example.com", "1111111111", "789 Main St", 28, "Designer", 45000))
# ad.view_employees()







