# difference among regular, static and class methods
# regular methods in a class automatically take the instance as the fist argument
# and by convention we were calling this self

# class methods automatically pass the cls as the first argument

# static methods do not pass anything automatically
# has a logical connection with the class but does not depend on any specific instance or class

class Employee:
    # class attributes
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)

    # adding a decorator
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    # alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True



print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'user', 60000)
# by using the class method we set the class variable
Employee.set_raise_amount(1.05)
# Same as
# Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2019, 7, 8)

print(Employee.is_workday(my_date))

# class methods can be used as alternative constructors
# static methods do not operate on the instance or the class
