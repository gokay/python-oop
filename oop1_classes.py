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
