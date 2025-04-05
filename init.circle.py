# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 10:30:34 2025

@author: HP
"""

class circle:
    def __init__(self,radius):
        self.__radius=radius
        
        
    def calculate(self):
            self.__area=3.14*self.__radius*self.__radius
            
    def display(self):
            print(f'Area of circle={self.__area}')
            
#object
cir1=circle(2)
cir1.calculate()
cir1.display()
