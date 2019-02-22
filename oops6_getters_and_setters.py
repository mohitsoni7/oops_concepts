"""
Basically, the main purpose of using getters and setters
in object-oriented programs is to ensure data encapsulation.

Different Underscores in Python
===============================
1. - (just underscore)
In interpreter it records the latest executed code

ex.
>>> a = 10
>>> b = 20
>>> _
ERROR
>>> a + b
>>> _
>>> _
30
>>> _ + 10
40
>>> _ * 10
400

2. name_ (trailing underscore)

It is used just to avoid conflict between similar looking different variables
ex. 
    name = "Mohit"
    name_ = "Mishi"

3. _name (leading single underscore)

It is known as "weak private" variable. It can be used to make some variable a semi-private as shown below.


"hey()" function will always run whether we directly execute this file or whether we import this file into another module.

"_hello()" function will only run if this file is directly run but it will not run if this file is imported in another module.

4. __name (leading double underscores)

It is used to make any attribute or method as "Private".
A private variable is only accessible inside a Class.

However, Python does not have a concept of "Strictly private".
ex.
__firstname = 'Mohit'

It can be accessed using "obj._ClassName__firstname"

5. __name__ (Double underscores or Donder methods)

These are special or magic methods in Python. 


"""


def hey():
    return 'Hey!!!'

# Private function (weak private)
def _hello():
    return 'Hello'

class Employee:

    _company = 'Ranosys'
    __ceo = 'RV'

    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname


    # Getter for firstname
    @property
    def firstname(self):
        return self.__firstname


    # Setter for firstname
    @firstname.setter
    def firstname(self, new_firstname):
        self.__firstname = new_firstname


    # Deleter for firstname
    @firstname.deleter
    def firstname(self):
        print('firstname deleted!')
        self.__firstname = None


    # Getter for lastname
    @property
    def lastname(self):
        return self.__lastname


    # Setter for lastname
    @lastname.setter
    def lastname(self, new_lastname):
        self.__lastname = new_lastname


    # Deleter for firstname
    @lastname.deleter
    def lastname(self):
        print('lastname deleted!')
        self.__lastname = None




    def fullname(self):
        return '{} {}'.format(self.__firstname, self.__lastname)


if __name__ == '__main__':
    emp_1 = Employee('Mohit', 'Soni')
    # print(emp_1.__firstname)
    print(emp_1.firstname)
    print(emp_1.lastname)
    print(emp_1.fullname())
    print(emp_1._company)
    print(Employee._company)
    # print(emp_1.__ceo)
    # print(Employee.__ceo)
    print(emp_1._Employee__ceo)
    # print(hey())
    # print(_hello())

    print(emp_1.fullname())
    emp_1.firstname = 'MOHIT'
    emp_1.lastname = 'SONI'
    print(emp_1.fullname())
    
    del emp_1.firstname
    print(emp_1.fullname())

    del emp_1.lastname
    print(emp_1.fullname())
