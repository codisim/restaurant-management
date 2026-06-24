from food_item import FoodItem
from menu import Menu
from users import User, Customer, Admin
from restaurant import Restaurant
from order import Order



mamar_restaurant = Restaurant("Mamar's Restaurant")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    
    customer = Customer(name, email, phone, address)
    
    
    while True:
        print(f"Welcome, {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. payBill")
        print("5. Exit")
        
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mamar_restaurant.view_menu()
        elif choice == 2:
            item_name = input("Enter the name of the item to add to cart: ")
            quantity = int(input("Enter the quantity: "))
            mamar_restaurant.add_to_cart(customer, item_name, quantity)
        elif choice == 3:
            mamar_restaurant.view_cart(customer)
        elif choice == 4:
            mamar_restaurant.pay_bill(customer)
        elif choice == 5:
            print("Thank you for visiting Mamar's Restaurant!")
            break
        



def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    
    admin = Admin(name, email, phone, address)
    
    
    while True:
        print(f"Welcome, {admin.name}!!")
        print("1. Add new item")
        print("2. Add  new employee")
        print("3. View employees")
        print("4. View items")
        print("5. Delete item")
        print("6. Exit")
        
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mamar_restaurant.view_menu()
        elif choice == 2:
            item_name = input("Enter the name of the item to add to cart: ")
            quantity = int(input("Enter the quantity: "))
            mamar_restaurant.add_to_cart(admin, item_name, quantity)
        elif choice == 3:
            mamar_restaurant.view_cart(admin)
        elif choice == 4:
            mamar_restaurant.pay_bill(admin)
        elif choice == 5:
            print("Thank you for visiting Mamar's Restaurant!")
            break