# Python OOP 4 Inheritance and subclasses
import datetime

class Employee:
    
    def __init__(self,first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def __repr__(self):
        return "Employee('{}','{}')".format(self.first,self.last)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('John','Smith')

emp_1.fullname = 'Gökay Gürsoy'

# emp_1.first = 'Mary'

print(emp_1.first)
# print(emp_1.email())
print(emp_1.email)
# print(emp_1.fullname())
print(emp_1.fullname)

del emp_1.fullname
