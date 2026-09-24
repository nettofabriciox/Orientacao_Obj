#class MinhaClass:
 #   x = 20
#p1 = MinhaClass()
#print(p1.x)  
# 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jose', 45)
print(p1.name, 'Tem anos: ', p1.age)