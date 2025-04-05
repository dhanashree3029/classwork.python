# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 19:29:39 2025

@author: HP
"""

#union of two sets.
#unique elements from the given sets.
set1,set2={1,2,3},{3,4,5,2}

#set1=set1.union(set1,set2)

#print(set1)

#intersection
#matched elements from the given sets.
#set1=set1.intersection(set1,set2)

#difference
#set1=set1.difference(set2)
#set2=set2.difference(set1)
#print(set2)

#symmetric_difference
#it will skip the matched elemnts from the given sets.
#set1=set1.symmetric_difference(set2)
#print(set1)

#issubset, issuperset

#s1={1,2,3,4,5,6}
#s2={1,2,3,4}
#issubset will return true when all the elements from s1
#are present in the set s2e;se return False print(s1.issubset(s2))

#issubset will return True when all the elements from s2
#are present in the s1,else return False print(s1.issuperset(s2))


#DICTIONARY

#d1={}
#print(d1)

d2={91:'IND',1:'USA'}

dept={101:'HR',102:'Sales',103:'Admin'}

d3={1:'Amol','marks':[78,67,66]}

#inner round bracket is to define one parameter.
d4=dict(([1,500],[2,499],[3,350]))
print(d4)

fruit={}

fruit['apple']=200
fruit['orange']=150

print(fruit)

fruit['orange']=250
print(fruit)
print(fruit.get('apple'))

print(dept.get(102))

dept={101:'HR',102:'Sales',103:'Admin'}

#iterate using for in loop
# .keys()

for key in dept.keys():
    print(key)
    
# .values() ->values will be extracted.

for value in dept.values():
    print(value)
    
#print both keys and values ->items()

for k,v in dept.items():
    print(f'{k}: {v}')
    
#dept.clear()
#print dept

#del dept
#del dept[103]  #103 is key
#print(dept)

#**kwargs
#def display(**data):
    #print(data)
    #for k,v in data.items():
        #print(f'{k}:{v}')
        
#display(age=30,city='Pune',rollno=1,per=78.88)



#class work.

#1.create a dictionary to hold employee data like id, name, salary.

#employee_data ={"Id": "101","Name":"siya","salary":"40000"}
#print(employee_data)

#print(employee_data.keys())
#print(employee_data.values())
#print(employee_data.items())


#Create a dictionary to hold product data ;ike code, name, price.

#dept ={"code": "200", "name": "rishi", "Price":"700"}
#print(dept)

#print(dept.keys())
#print(dept.values())
#print(dept.items())


#Delete one product in the existing dictionary.
#dict = {'name' :'rahul', 'class' :'5', 'age': '8'}
#del dict['age']
#print(dict)

#add one product in the dict.
#employees1 ={1:'amol',2:'rani'}
#employees2 ={2:'jojo'}
#print (employees1,employees2)



# Assessments on Dictionary.

# 1. Wap to combine two dictionary adding values for common keys.
d1={'a':100, 'b':200, 'c':300}
d2={'a':300, 'b':200, 'd':400}

d3=d1.copy()
d3.update(d2)

for key in d2:
    if key in d1:
        d3[key]=d2[key]+d1[key]
print(d3)