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

