#inheritance of employee from manager.

#class Employee:
 #   manager class inherit from emp class:
        
class Employee:
     def __init__(self,name,salary):
         self.name=name
         self.salary=salary
         
     def display_info(self):
         return f"{self.name}:{self.salary}"
         
class Manager(Employee):
     def __init__(self,name,salary,department):
         super().__init__(name,salary)
         self.department=department
         
     def display_info(self):
        return f"{self.name}.(Manager):{self.salary},department:{self.department}:"
    
#object
employee1 = Employee("Amol",50000)
Manager = Manager("sia",80000,"Sales")

print(employee1. display_info())
print(Manager. display_info())
    







            
    
    
