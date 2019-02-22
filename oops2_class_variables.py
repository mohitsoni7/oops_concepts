"""
	Class Variables
	===============

	The variables which are shared among all the instances of a Class are Class Variables.

	

	Instance Variables
	==================

	The variables which are Unique for each instance.

	
	Flow
	====
	1. Any variable is searched in the instance. It uses it if found!!!
	2. If not found, it is searched in the parent class
	3. If not found, displays ERROR!!! 


"""

class Employee:

	# Class Variables

	raise_amount = 1.04

	def __init__(self, firstname, lastname, pay):

		# Instance Variables

		self.firstname = firstname
		self.lastname = lastname
		self.pay = pay
		# automatically generated
		self.email = firstname.lower() + '.' + lastname.lower() + '@ranosys.com'


	def fullname(self):
		return '{} {}'.format(self.firstname, self.lastname)

	
	def apply_raise(self):
		# 1st way
		self.pay = int(self.pay * self.raise_amount)

		# 2nd way
		# self.pay = int(self.pay * Employee.raise_amount)


emp1 = Employee('Mohit', 'Soni', 50000)
emp2 = Employee('Anuj', 'Katara', 50000)

# print(emp1.fullname())
# print(emp1.email)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)


# print(Employee.__dict__)
# print(emp1.__dict__)
print("Class variable accessed from class_name: ", Employee.raise_amount)
print("Class variable inherited in instance from Class: ", emp1.raise_amount)

# Only change the Instance Attributes
print('-------Instance attribute applied for emp1 as 1.05------')
emp1.raise_amount = 1.05
# print(emp1.__dict__)
print("Class variable accessed from class_name: ", Employee.raise_amount)
print("Instance variable overridden from instance: ", emp1.raise_amount)


# It changes the Class Attribute
print('-------Class attribute changed to 1.07------')
Employee.raise_amount = 1.07
print("Class variable accessed from class_name: ", Employee.raise_amount)
print("Class variable inherited in instance from Class: ", emp2.raise_amount)

