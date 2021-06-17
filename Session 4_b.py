# how class variables differ from instance variables
# class variables are variables that are shared among all instances of a class
# while instance variables can be unique for each instance
# class variables should be the same for each instance

class Employee:
    # class attribute
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"
        # __init__ method runs everytime we craete a new instance/employee

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'user', 60000)

print(Employee.num_of_emps)

print(emp_1.pay)
emp_1.apply_raise()
print(int(emp_1.pay))

# I can access this class variable from both my class itself and from both of the instances
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print out the namespace of the instance emp_1 and our class Employee
# we don't see the class atrribute in the instance
print(emp_1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05
# Change the raise amount for the class and all the instances
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.08
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# we learned the difference between instance variables and class variables
