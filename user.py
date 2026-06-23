
from abc import ABC
from order import Order
from menu import Menu, MenuItem
from restaurent import Restaurant


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
        self.card = Order()
        
    def view_menu(self, restaurant):
        restaurant.menu.view_menu()
        
    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeds available stock.")
            item.quantity = quantity
            self.card.add_item(item)
        else:
            print(f"Item '{item_name}' not found in the menu.")
            
            
    def view_cart(self):
        print("Cart Items:")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.card.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        
        print(f"Total Price: {self.card.total_price()}")
        
        
    def pay_bill(self, restaurant):
        total = self.card.total_price()
        print(f"Total Bill: {total}")
        # Here you can implement payment logic (e.g., deducting from a balance, processing payment, etc.)
        self.card.clear()
        print("Payment successful. Thank you for your order!")
        
        
        

class Order():
    def __init__(self):
        self.items = {}
        
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
            
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"Item '{item.name}' not found in the cart.")
            
    
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items()) 
    
    def clear(self):
        self.items = {}
        
        
        
        

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
        
    





    

mamar_res = Restaurant("Mamar Restaurant")
    
mn = Menu()
item1 = MenuItem("Pizza", 10.99, 20)
item2 = MenuItem("Burger", 5.99, 30)
item3 = MenuItem("Pasta", 8.99, 25)

admin = Admin("Admin", "admin@example.com", "0987654321", "456 Admin St")
admin.add_menu_item(mamar_res, item1)
admin.add_menu_item(mamar_res, item2)
admin.add_menu_item(mamar_res, item3)


customer1 = Customer("Alice", "alice@example.com", "1234567890", "123 Main St")
customer1.view_menu(mamar_res)


input_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))

customer1.add_to_cart(mamar_res, input_name, item_quantity)
customer1.view_cart()
























# ad = Admin("Admin", "admin@example.com", "0987654321", "456 Admin St")
# restaurant = Restaurant("My Restaurant")
# ad.add_employee(restaurant, Employee("Rahim", "rahim@example.com", "1234567890", "123 Main St", 30, "Manager", 50000))
# ad.add_employee(restaurant, Employee("Karim", "karim@example.com", "0987654321", "456 Main St", 25, "Developer", 40000))
# ad.add_employee(restaurant, Employee("Jamal", "jamal@example.com", "1111111111", "789 Main St", 28, "Designer", 45000))
# ad.view_employees()







