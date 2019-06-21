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
### Class methods and staticmethods
### Inheritance
### Magic / Dunder methods
### Decorators, getters, setters, deleters

