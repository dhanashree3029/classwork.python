#hierarchical inheritance.

#Base class.
class Bank:
    def __init__(self,name):
        self.name = name
        
class saving(Bank):
    def acount_number(self):
        return "1234"
class current(Bank):
    def acount_number(self):
        return"5678"
        
#CREATING OBJECTS
saving = saving("balance")
current =current("amount")

#accessing methods
print(saving.name)
print(current.name)
        
    
#hierarchy of vehicle.
class Vehicle:
    def show_info(self):
        print('You have a Vehicle')        
        
class bike(Vehicle):
    def show_info(self):
        print('bike')
        
class car(Vehicle):
    def show_info(self):
        print('car')
        
b=bike()
b.show_info()

c=car()
c.show_info()



        
        

