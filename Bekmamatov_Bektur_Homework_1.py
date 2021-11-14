class Zoo():
    def init(self, habitat, was_born):
        self.habitat = habitat
        self.was_born = was_born
    def str(self):
        return f'Habitat: {self.habitat}\n'\
               f'Was_born: {self.was_born}\n'\
        
class Animals():
    def init(self, name, age, type, color):
        self.name = name
        self.age = age
        self.type = type
        self.color = color
    def str(self):
        return  f"Name: {self.name}\n"\
                f"Age: {self.age}\n"\
                f"Type: {self.type}\n"\
                f"Color: {self.color}\n"\

class ZooShow(Zoo, Animals):
    def init(self, habitat, was_born, cost):
        super().init(habitat, was_born)
        self.cost = cost
    def str(self):
        return f"Cost: {self.cost}\n"\

Camel =    Animals(name="Camel", age="6 month", type="herbivores", color="brown")
Elephant = Animals(name="Elephant", age="1 years", type="herbivores", color="gray")
Horse =    Animals(name="Horse", age="2 years", type="herbiroves", color="black")
                

Snake =     Animals(name="Snake", age="4 years", type="predators", color="green",)
Crocodile = Animals(name="Crocodile", age="3 years", type="predators", color="green")
Lion =      Animals(name="Lion", age="6 years", type="predators", color="yellow")

cost = ZooShow(Camel = "20$", Elephant = "25$", Horse = "15$", Snake = "40$", Crocodile = "50$", Lion = "55$")

print(Snake)