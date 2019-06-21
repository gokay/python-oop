# Python OOP 4 Inheritance and subclasses
import datetime

class Employee:
    
    raise_amount = 1.04

    def __init__(self,first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last
    
    def apply_araise(self):
        self.pay = int(self.pay  * self.raise_amount)
    
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first, last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,first, last,pay,employees = None):
        super().__init__(first,last,pay)

        if employees is None:
            self.empoyees  =[]
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ' + emp.fullname())
       

emp_1 = Employee('Gökay','Gürsoy',80000)
emp_2 = Employee('John', 'Travolta', 50000)

print(emp_1 + emp_2)

print(len('test'))

print(len(emp_1))


# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())

