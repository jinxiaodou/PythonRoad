class Person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def eat(self):
        print('是人都会吃')
    
    def __str__(self):
        return '我是一个Person，名叫'+self.name+',年龄'+str(self.age)

class Animal(object):
    def __init__(self,sex):
        self.sex=sex
    
    def bellow(self):
        print('是动物就会叫')
    
    def __str__(self):
        return '我是一个Animal，性别'+self.sex

class Kid(Person,Animal):
    def __init__(self,name,age,sex,color):
        Person.__init__(self,name,age)
        Animal.__init__(self,sex)
        self.color=color
    
    def cry(self):
        print('小孩都会哭')
    
    def __str__(self):
        return '我是一个Kid,名叫'+self.name+', 年龄'+str(self.age)+',性别'+self.sex+',颜色'+self.color

person=Person('大明',33)
person.eat()
print(person)

animal=Animal('男')
animal.bellow()
print(animal)

kid=Kid('小明',2,'男','黄')
kid.bellow()
kid.eat()
kid.cry()
print(kid)