"""
Here we will make a base class named: Employee

Then we will make 2 child class of it viz. Developer & Manager
"""

class Employee:
    # Parent class

    raise_amt = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname.lower() + '.' + lastname.lower() + '@yopmail.com'

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    # Child class of Employee

    raise_amt = 1.10

    # If we want some extra parameters in our child class then
    # we can make the __init__ method of the child class too.

    # Where we will leave the default variables of Parent class as it is
    # We will add extra variables
    # Then we will overide the Parent class
    def __init__(self, firstname, lastname, pay, tech):
        # 1st way using super()
        super().__init__(firstname, lastname, pay)
        self.tech = tech
        # 2nd way using Parent_class_name
        # Employee.__init__(self, firstname, lastname, pay)
        # self.tech = tech

class Manager(Employee):

    raise_amt = 1.05

    def __init__(self, firstname, lastname, pay, devs=None):
        super().__init__(firstname, lastname, pay)
        if devs is None:
            self.devs = []
        else:
            self.devs = devs

    def add_dev(self, dev):
        if dev not in self.devs:
            self.devs.append(dev)

    def remove_dev(self, dev):
        if dev in self.devs:
            self.devs.remove(dev)



print('Developer will get a raise of 10% by overiding the default 4% raise_amt of its parent class')
emp_1 = Employee('R', 'V', 1000000)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# dev_1 = Developer('Mohit', 'Soni', 90000)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


dev_1 = Developer('Mohit', 'Soni', 90000, 'Python')
print(dev_1.tech)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

dev_2 = Developer('Ankit', 'Arora', 95000, 'Java')


mgr_1 = Manager('Ashish', 'Solanki', 99000)
print('----------------------------------------')
print('Now {} manages:'.format(mgr_1.fullname()))
for dev in mgr_1.devs:
    print('-->', dev.fullname())

print('----------------------------------------')

print('Add a dev under manager')

mgr_1.add_dev(dev_1)
print('Now {} manages:'.format(mgr_1.fullname()))
[print('-->', dv.fullname()) for dv in mgr_1.devs]


print('----------------------------------------')

print('Add another dev under manager')
mgr_1.add_dev(dev_2)
print('Now {} manages:'.format(mgr_1.fullname()))
[print('-->', dv.fullname()) for dv in mgr_1.devs]


print('----------------------------------------')

print('Remove a dev under manager')
mgr_1.remove_dev(dev_1)
print('Now {} manages:'.format(mgr_1.fullname()))
[print('-->', dv.fullname()) for dv in mgr_1.devs]

print('----------------------------------------')

print('Check if "dev_1" is an instance of class "Developer"')
print(isinstance(dev_1, Developer))

print('Check if "dev_1" is an instance of class "Employee"')
print(isinstance(dev_1, Employee))

print('Check if "dev_1" is an instance of class "Manager"')
print(isinstance(dev_1, Manager))

print('----------------------------------------')

print('Check if "Developer" is a subclass of class "Manager"')
print(issubclass(Developer, Manager))

print('Check if "Developer" is an subclass of class "Employee"')
print(issubclass(Developer, Employee))

print('Check if "Manager" is an subclass of class "Employee"')
print(issubclass(Manager, Employee))

print('Check if "Employee" is an subclass of class "Employee"')
print(issubclass(Employee, Employee))