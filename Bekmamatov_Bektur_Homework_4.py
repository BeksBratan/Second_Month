# Задание № 1


class TimeDesk:
    def __init__(self, seconds):
        self.seconds = seconds
    
    def sec_time(self):
        days = self.seconds // 86400
        self.seconds -= 86400*days

        hours = self.seconds // 3600
        self.seconds -= 3600*hours

        min = self.seconds // 60
        self.seconds -= 60*min

        results = ["days : {}  , hours : {}  , min : {}  , sec : {}".format(days, hours, min, self.seconds)]
        return results

t = TimeDesk(70)
print(t.sec_time())


# Задание № 2


class Human:
    def __init__(self, name, age, was_born):
        self.name = name
        self.age = age
        self.was_born = was_born
    

    @property
    def information(self):
            i = f'His information : {self.name}, {self.age}, {self.was_born} '
            return i
    
    @information.setter
    def information(self, info):
        self.name, self.age, self.was_born = info.split()
    
    @information.deleter
    def information(self):
        self.was_born = None
        print("When he worn , was deleted")

    @staticmethod
    def calculator():
        number = 2*(4+5-4+1+3)
        return number
        

    def __str__(self):
        return  f'Name : {self.name}\n'\
                f'Age : {self.age}\n'\
                f'Was_born : {self.was_born}\n'\

a = Human(name="Alex", age="17", was_born="USA")
print(a)
print(a.information)
a.name = "Alina"
a.age = "20"
print(a.information) 
del a.information
print(a.information)
print(a.calculator())


    


    
    

    




    




        
