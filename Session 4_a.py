# Python Object-Oriented Programming
# data and functions associated with a class, we call those attributes and methods

class Employee:
    # init method takes the instance which we called self,
    # then takes first, last, and pay as arguments or attributes of our class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    # each method within a class automatically takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# pass

# unique instances of the employee class
# instance is passed automatically, we only need to provide names and pay
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'user', 60000)

# # each of these instances now have attributes that are unique to them
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'coray.schafer@company.com'
# emp_1.pay = 50000
#
# emp_1.first = 'Test'
# emp_1.last = 'User'
# emp_1.email = 'test.user@company.com'
# emp_1.pay = 60000

# print('{} {}'.format(emp_1.first, emp_1.last))

print(emp_1.email)
print(emp_2.email)

# we need parenthesis because this is a method
# instance argument (emp_1) is passed automatically
print(emp_1.fullname())

# We can also run these methods using the class name itself
print(Employee.fullname(emp_2))

# creating simple class
# difference between a class and an instance of that class
# how to initialize class attributes and create methods


