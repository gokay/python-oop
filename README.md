![](https://github.com/gokay/python-oop/blob/master/python-logo.png)

# Python 3.7.x OOP basics


## For [Python 3.7.x](https://docs.python.org/3.7/library/index.html) documentation

## [Padao](https://pandao.github.io/editor.md/en.html) markdown editor used for this file


# Table of Contents


1. [Classes](#classes)
2. [Class variables](#class-variables)
3. [Class methods and staticmethods](#class-methods-and-staticmethods)
4. [Inheritance](#inheritance)
5. [Magic / Dunder methods](#magic-dunder-methods)
6. [Decorators, getters, setters, deleters](#Decorators-getters-setters-deleters)


### Classes
```python
# Python OOP 1 Classes

class Employee:
    def __init__(self,first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return self.first + ' ' + self.last
    

empl_1 = Employee('Gökay','Gürsoy',50000)
empl_2 = Employee('İpek','Gürsoy',90000)

# print(empl_1)
# print(empl_1)

# print(empl_1.email)
# print(empl_2.email)

# print('{} {}'.format(empl_1.first,empl_1.last))
print (empl_1.fullname())

print(Employee.fullname(empl_1))

```

### Class variables
```python
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

print(Employee.num_of_emps)

empl_1 = Employee('Gökay','Gürsoy',50000)
empl_2 = Employee('İpek','Gürsoy',90000)

print(Employee.num_of_emps)
# print(Employee.raise_amount)
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)

print(empl_1.__dict__)
print(Employee.__dict__)


# print(empl_1)
# print(empl_1)

# print(empl_1.pay)
# empl_1.apply_araise()

# print(empl_2.pay)

# # print('{} {}'.format(empl_1.first,empl_1.last))
# print (empl_1.fullname())

# print(Employee.fullname(empl_1))

```

### Class methods and staticmethods
```python
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

```

### Inheritance
```python
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

        

dev_1 = Developer('Gökay','Gürsoy',80000,'Python')
dev_2 = Developer('John', 'Travolta', 50000,'Java')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])

# print(mgr_1.email)

# # mgr_1.print_emps()

# mgr_1.add_employee(dev_2)
# mgr_1.remove_emp(dev_2)
# mgr_1.print_emps()


# print(isinstance(mgr_1,Employee))
# print(isinstance(mgr_1,Manager))
# print(issubclass(Manager,Manager))
print(issubclass(Manager,Employee))



# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_araise()
# print(dev_1.pay)

```
### Magic / Dunder methods
```python
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

```
### Decorators, getters, setters, deleters
```python
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

```

