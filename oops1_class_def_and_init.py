
# Trciky question 1: Do you strictly use "self" or can you use some custom name?
# Ans: No, its just a convention

"""
    Following example demonstrate the above concept,
    where I have used "mohit" instead of "self"
"""

class Developer:

    def __init__(mohit, firstname, lastname):
        mohit.firstname = firstname
        mohit.lastname = lastname


# Tricky question 2: Do you strictly require "self.firstname" or
# can you use some custom variable?
#Ans: No, its just a convention


"""
    Following example demonstrate the above concept,
    where I have used "mohit" instead of "self"
"""

class Person:

    def __init__(yoyo, firstname, lastname):
        yoyo.fname = firstname
        yoyo.lname = lastname

#Also, below is valid obviously

class Player:

    def __init__(yoyo, fname, lname):
        yoyo.firstname = fname
        yoyo.lastname = lname


class Employee:

    def __init__(self, firstname, lastname):
        # attributes
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)


if __name__ == '__main__':
    dev1 = Developer('Elon', 'Musk')
    print(dev1)
    print(dev1.firstname)
    print(dev1.lastname)

    per1 = Person('Virat', 'Kohli')
    print(per1)
    print(per1.fname)
    print(per1.lname)

    player = Player('Rohit', 'Sharma')
    print(player)
    print(player.firstname)
    print(player.lastname)


    """ 
        By default, 1st way is convenient but
        inside 1st way operates like the 2nd way.
    """
    emp1 = Employee('Mohit', 'Soni')
    print(emp1.firstname)
    # 1st way
    print(emp1.fullname())
    # 2nd way
    print(Employee.fullname(emp1))