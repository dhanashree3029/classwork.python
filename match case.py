# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 18:42:10 2025

@author: HP
"""

#print('1. english')
#print('2. hindi')
#print('3. marathi')

#options=int(input('select your option :'))

#match option:
   #case 1:print('you have selected eng')
   #case 2:print('you have selected hindi')
   #case 3:print('you have selected marathi')
   #case default:print('wrong option selected')
   
   
   
a=10
b=20
c=30

if a<b:
    if b<c:
        if a<c:
            print('inside the nested block')
        else:
           print('else block')
    else:
        print('')
else:
    print('')
    
# OR --> logical

if a<b and a<c and b<c:
    print('true block')
        
    
   