# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 10:52:58 2025

@author: HP
"""

#create product type dict.
#add 5% product of ech product
#display product whose price  < 1000

product={
    "chocolate":1500,
    "cookies":1300,
    "chocos":900,
    "cakes":1400
    }

new_product=dict(map(lambda item:(item[0],item[1]*1.5 if item [1]>1000 else item[1])
                ,product.items()))
print(new_product)

filter_product=dict(filter(lambda item:item[1]>1000,product.items()))
print(filter_product)

