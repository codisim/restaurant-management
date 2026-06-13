
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
        self.employees = []

    
