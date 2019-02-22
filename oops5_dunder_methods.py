"""
    Dunder methods / Magic methods / Special methods
    ================================================

    These are special methods which are responsible for the certain types of behaviour of
    objects of every class.

    Also, these methods are responsible for the concept of "Operator overloading".


    Operator overloading
    --------------------
    It means we can make operators to work for User defined classes.

    For ex. "+" operator works differently for Integers and Strings.

    Similarly, we can make it work in our way for our User defined Class.

    __repr__ method
    ---------------
    It gives the "Unambiguous" representation of an instance of a class.

    Usually, helps and is used in debugging, logging etc.
    Used by developers!

    __str__ method
    ---------------
    It gives the "End user readable" representation of an instance of a class.

    Note: If __str__ method is not there then a call to __str__ method, fallback to __repr__ method.
    i.e. str(emp_1) and repr(emp_1) will give the same output.
"""


class Employee:

    raise_amt = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname.lower() + '.' + lastname.lower() + '@yopmail.com'


    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)


    def apply_raise(self):
        self.pay = (self.pay * self.raise_amt)


    def __repr__(self):
        return "Employee({}, {}, {})".format(self.firstname, self.lastname, self.pay)


    # def __str__(self):
    #     return 'Employee: {}'.format(self.fullname())

    # Operator overloading

    # Here, we are overloading the "+" operator
    # We are making it work such that if 2 instances of class Employee are added,
    # there salaries are added.
    def __add__(self, other):
        return int(self.pay + other.pay)


    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Mohit', 'Soni', 70000)
print(emp_1)
print(emp_1.__repr__())
print(Employee.__repr__(emp_1))
# print(emp_1.__str__())
print(repr(emp_1))
print(str(emp_1))

emp_2 = Employee('Udit', 'Soni', 80000)
print(emp_1 + emp_2)
print(Employee.__add__(emp_1, emp_2))

print(len(emp_1))