# Python OOP 2 Class Variables

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