
class Matematik:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def topla(self): #! search "self"
        return self.x+self.y
    def cıkart(self):
        return self.x-self.y
    def carp(self):
        return self.x*self.y
    def bol(self):
        return self.x/self.y
    def mod(self):
        return self.x % self.y

matematik = Matematik(2,78)
matematik2 = Matematik(3,76)
print(str(matematik2.topla()))

#? Property

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Engin","Demiroğ",33)
print(person1.firstName)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary

class Customer(Person):
    def __init__(self,creditCaradNumber):
        self.creditCardNumber = creditCaradNumber
    
person2 = Worker()
person3 = Customer()

