# Python OOP 3 Class classmethods and staticmethods
import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + ' ' + self.last
    
    def apply_araise(self):
        self.pay = int(self.pay  * self.raise_amount)

    @classmethod
    def set_araise_amt(cls, amout):
        cls.raise_amount = amout

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

my_date = datetime.date(2019,6,17)

print(Employee.is_workday(my_date))


# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Jobs-30000'
# emp_str_3 = 'Mary-Jane-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# new_emp_2 = Employee.from_string(emp_str_2)
# print(new_emp_2.email)
# print(new_emp_2.pay)

