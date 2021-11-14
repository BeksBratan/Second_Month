# Задача №1 Наследование
class Child:
    def __init__(self, name, age, hairs, weight):
        self.name = name
        self.age = age
        self.hairs = hairs
        self.weight = weight
        
    def my_name(self):
        return f'My name is : {self.name}'
    
    def __str__(self):
        return  f'His Name is : {self.name}\n'\
                f'His Age is : {self.age}\n'\
                f'His Hairs are : {self.hairs}\n'\
                f'His Weights : {self.weight}\n'\
               
child = Child(name="Jon", 
              age="1 years",
              hairs="Black",
              weight="10 kilo")
     

class Son(Child):
    def __init__(self, name, age, hairs, weight, height):
        super().__init__(name, age, hairs, weight)
        self.height = height

    def __str__(self):
        return super(Son, self).__str__() + f'His heights : {self.height}\n'\
    
son = Son(name="Jack", 
            age="10 years",
            hairs="Black",
            weight="50 kilo",
            height="165")


class Dad(Son):
    def __init__(self, name, age, hairs, weight, height, job):
        super().__init__(name, age, hairs, weight, height)
        self.job = job

    def __str__(self):
        return super(Dad, self).__str__() + f'His jobs is a : {self.job}\n'\

dad = Dad(name="Jony", 
            age="32 years",
            hairs="Black",
            weight="80 kilo",
            height="186",
            job="Doctor")
# print(child)
# print(child.my_name)
# print(son)           
# print(dad)



# Задача №2 Инкапсуляция
class Alina:
    def init(self, name):
        self.name = name

    def __Phone(self):
        print("This private information for you!!!") 

    def _mame(self):
        print(f"Her name is {self.name}")

alina = Alina(name="Alina")
# print(alina.__Phone())
# print(alina._Name())


# Задача № 3 Полиморфизм без наследования

class Spider_Man:
    def attack(self):
        print("Spider-Man attacks with cobwebs")

class Thor:
    def attack(self):
        print("Thor attacks with hammer")

class Hawkeye:
    def attack(self):
        print("Hawkeye attacks with bow")

# spider_man = Spider_Man()
# spider_man.attack()

# thor = Thor()
# thor.attack()

# hawkeye = Hawkeye()
# hawkeye.attack()

# Задача № 4 Полиморфизм с наследованием
class Spider_man2:
    def attack(self):
        print("Spider-Man attacks with cobwebs")

class Thor2(Spider_Man):
    def attack(self):
        print("Thor attacks with hammer")

class Hawkeye2(Thor):
    def attack(self):
        print("Hawkeye attacks with bow")

spider_man2 = Spider_man2()
spider_man2.attack()
thor2 = Thor2()
thor2.attack()
hawkeye2 = Hawkeye2()
hawkeye2.attack()





    
 

        



