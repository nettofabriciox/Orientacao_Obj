#class MinhaClass:
 #   x = 20
#p1 = MinhaClass()
#print(p1.x)  
# 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input('Entre com nome: ')
age = input('Entre com valor: ')
p1 = Person(name, age)
print(p1.name)
print(p1.age)