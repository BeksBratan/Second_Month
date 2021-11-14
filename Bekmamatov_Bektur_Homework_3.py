# Задание № 1 Множественное Наследование (Ромбовидный)



class Programmer:
    def __init__(self, type, level, experience, language, price):
        self.type = type
        self.level = level
        self.experience = experience
        self.language = language
        self.price = price
    
    def his_level(self):
        return f'My level is {self.level} '
    def type_of_programming(self):
        return f"I'm a {self.type} developer"

    def __str__(self):
        return f'\n\nHe is a {self.type} developer\n'\
               f'His level is {self.level}\n'\
               f'He has {self.experience} of work experience\n'\
               f'He Knows {self.language} language\n'\
               f'I earn {self.price} per month'

person_1 = Programmer(type="Front-end", level="First", experience="1 years", language="JavaScript", price="1000$") 
# print(person_1)





class Level_2(Programmer):
    def his_levels(self):
        return f'\nMy level is {self.level} '
    def knows_languages(self):
        return f'\nI know {self.language} language'
    
    def __str__(self):
        return super(Level_2, self).__str__() 
    
person_2 = Level_2(type="Back-end", level="Second", experience="3 years", language="Python", price="1000$")
# print(person_2)



class Level_3(Programmer):
    def info(self):
        return f'\nHe knows {self.language} and he is {self.type} developer'
    
    def __str__(self):
        return super(Level_3, self).__str__()
    
person_3 = Level_3(type="Android", level="3", experience="3,5 years", language="Java", price="2000$")
# print(person_3)




class Level_4(Level_2, Level_3):
    def How_long_working(self):
        return f'\nI have been working {self.experince}'

    def __str__(self):
        return super(Level_4, self).__str__() 

person_4 = Level_4(type="FullStack", level="4", experience="10 years", language="Python and JavaScript", price="6000$")
# print(person_4)

# print(person_4.info())










# Задание № 2 Множественное Наследование ( Один ко многим )

class Phone:
    def __init__(self, name, model, color, memory,):
        self.name = name
        self.model = model
        self.color = color
        self.memory = memory

    def __str__(self):
        return f'\nName : {self.name}\n'\
                f'Model : {self.model}\n'\
                f'Color : {self.color}\n'\
                f'Memory : {self.memory}\n'


class Iphone(Phone):
    def __init__(self, name, model, color, memory, production):
        super().__init__(name, model, color, memory)
        self.production = production
    
    def __str__(self):
        return super(Iphone, self).__str__() + f'Production : {self.production}'
    
    def top(self):
        return f'{self.name} is the best phone in 2020'

phone_1 = Iphone(name="Apple", model="Iphone 13 pro max", color="White", memory="256gb", production="China")
# print(phone_1)


class Samsung(Phone):
    def __init__(self, name, model, color, memory, cost):
        super().__init__(name, model, color, memory)
        self.cost = cost

    def __str__(self):
        return super(Samsung, self).__str__() + f'Cost : {self.cost}'
    
    def a(self):
        return f'OMG my phone cost {self.cost}'

phone_2 = Samsung(name="Samsung", model="Galaxy Z Fold3", color="Black", memory="512gb", cost="156.000 сом")
# print(phone_2)


class Mi(Phone):
    def __init__(self, name, model, color, memory, release):
        super().__init__(name, model, color, memory)
        self.release = release
    
    def __str__(self):
        return super(Mi, self).__str__() + f'Release : {self.release}'
    
    def b(self):
        return f'I think {self.color} so beatiful'

phone_3 = Mi(name="Mi", model="Mi 8 lite", color="Blue", memory="128gb", release="2018")
# print(phone_3)





# Задание № 3 Магические методы

class Cinema:
    def __init__(self, name, ticket, years):
        self.name = name
        self.ticket = ticket
        self.years = years

    def __add__(self, other):
        if isinstance(other , list):
            other.append(self)
            return other
        else:
            return [self, other]
    
    def __str__(self):
        return f'Name : {self.name}\n'\
                f'Ticket : {self.ticket}\n'\
                f'Years : {self.years}\n'\

moana = Cinema(name="Moana", ticket="15", years="2017")
cinderella = Cinema(name="Cinderella",ticket= "20", years="2014")
legeds = Cinema(name="Legeds", ticket="10", years="2021")


class Starbuks:
    def __init__(self, starbuks, *names):
        self.starbucks = starbuks
        self.names = []
        for i in names:
            self.names.append(i)

    def __len__(self):
        return len(self.names)

    def __add__(self, name):
        self.names.append(name)
        return self

    def __sub__(self, other):
        self.names.append(other)
        return self

    def showCoffee(self):
        print("Имя на кофе")
        print("------------")
        for name in self.names:
            if (len(name) > 5):
                print(name, " - ", name[0:5])
            else:
                print(name, " - ", name)

    def showCoffee(self, name):
        if (len(name) > 5):
            print(name, " - ", name[0:5])
        else:
            print(name, " - ", name)


menu = Starbuks("Starbuks 2", "Alinas", "Annaas", "Victaa")
print(len(menu))
menu = menu + "Alx"
menu.showCoffee()



              


                

