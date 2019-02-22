"""
    regularmethod
    ==============
    Regular methods in a class automatically takes the "instance" as the first argument.
    By convention we were calling it as "self".

    It can also be called as "intance method"


    classmethod
    ============
    Class methods takes the "class" as the first argument.
    For making a "regularmethod" into a "classmethod" we need a decorator @classmethod

    "We can run a class method from an instance too but it does not make any sense."

    Note: Classmethods can be used as "alternative constructors" too.

    It means we can use these classmethods to provide multiple ways of creating objects.

    example:
    If we have users are in a list where names are saved as "mohit-soni-75000".
    We need to save these users.
    We can use classmethods in order to do that.


    staticmethod
    =============
    Staticmethods takes neither "instance" nor "class" as argument.

    They are just normal functions which have some logical connection with the class.

    We can determine a particular method as "staticmethod" by checking that
    in the entire method "instance" or "class" are not getting used.
    Then we can say that it is appropriate as a staticmethod.
"""

class Employee:

    no_of_employees = 0
    raise_amount = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname.lower() + '.' + lastname.lower() + '@ranosys.com'

        Employee.no_of_employees += 1


    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


    @classmethod
    def from_string(cls, emp_str):
        # usually 'from_methodname' is convention
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)


    @staticmethod
    def is_workday(day):
        print(day.weekday())
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Mohit', 'Soni', 50000)
emp2 = Employee('Anuj', 'Katara', 55000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print('=================')
print('Change the raise amount to 1.05')
print('=================')
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print('==================')
print('We can run a class method from an instance too but it does not make any sense.')
print('Change the raise amount to 1.07 from "instance"')
print('==================')

emp1.set_raise_amt(1.07)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)


print('==================')
print('Classmethods used as alternaive constructors')
print("""
    We are providing emp_str as input and
    our "alternaive_constructor" will create objects using it automatically""")
print('==================')

print('Input strings are as follows:')
emp_str_1 = 'Jhon-Doe-70000' 
emp_str_2 = 'Jane-Doe-75000' 
emp_str_3 = 'Steve-smith-65000'
print(emp_str_1)
print(emp_str_2)
print(emp_str_3)

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.fullname())
print(new_emp_2.fullname())
print(new_emp_3.fullname())

print('==================')
print('Check static method to check whether someday is workday or not')
print('==================')

import datetime
my_date = datetime.date(2019, 5, 10)
my_date_2 = datetime.date(2019, 10, 6)

print(Employee.is_workday(my_date))
print(new_emp_1.is_workday(my_date_2))
