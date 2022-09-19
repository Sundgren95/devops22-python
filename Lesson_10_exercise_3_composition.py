# Exercise 3 composition

class Address:
    def __init__(self, street_name, street_number, postal_code, country):
        self.street_name = street_name
        self.street_number = street_number
        self.postal_code = postal_code
        self.country = country

class Employee:
    def __init__(self, address, employee_number, salary):
        self.address = address
        self.employee_number = employee_number
        self.salary = salary