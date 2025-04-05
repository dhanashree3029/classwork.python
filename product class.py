# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 20:58:22 2025

@author: HP
"""

# Create product class accept code, name,price,give 20% discount if price is
#>10000,,5k-10k 15% discount, below 5k 5% discount.
# Display code, name,actualprice & discounted price.

class Product:
    def accept(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        
    def calculate__discount(self):
        if self.price > 10000:
            return 0.15 *self.price
        elif 5000 >= self.price <=10000:
            return 0.15 * self.price
        else:
            return 0.05 *self.price
    def display(self):
        discount = self.calculate__discount()
        discounted__price =self.price-discount
        print("Code:",self.code)
        print("Name:",self.name)
        print("Actual Price:", self.price)
        print("Discounted price:",discounted__price)
        
#object
product1 = Product()
product1.accept(601,"TV",12000)
product1.display()

product2 = Product()
product2.accept(602,"AC",15000)
product2.display()

product3 = Product()
product3.accept(603,"PC",12000)
product3.display()


        