from menu import Menu, MenuItem
from user import User, Customer, Admin
from restaurent import Restaurant
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
            item_name = input("Enter the name of the item: ")
            item_price = float(input("Enter the price of the item: "))
            item_quantity = int(input("Enter the quantity of the item: "))
            new_item = MenuItem(item_name, item_price, item_quantity)
            admin.add_menu_item(mamar_restaurant, new_item)
            
        elif choice == 2:
            employee_name = input("Enter the name of the employee: ")
            employee_email = input("Enter the email of the employee: ")
            employee_phone = input("Enter the phone number of the employee: ")
            employee_address = input("Enter the address of the employee: ")
            new_employee = Customer(employee_name, employee_email, employee_phone, employee_address)
            admin.add_employee(new_employee)
            
        elif choice == 3:
            admin.view_employees(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter the name of the item to delete: ")
            admin.delete_item(mamar_restaurant, item_name)
        elif choice == 6:
            print("Thank you for visiting Mamar's Restaurant!")
            break