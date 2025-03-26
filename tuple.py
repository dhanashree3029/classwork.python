# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 10:54:46 2025

@author: HP
"""

#t1=(1,2,3,4,5)

#t2=('Hello',70,[10,20,30],(1,2,3))

#print(t2[2][1])

#print(t2[1])

#print(t2[3])
#print(t2[3][2])

#t1[1]=20

#print(t1)

#t3=(10)

#t4=(10,)

#print(type(t3))
#print(type(t4))

#unpacking

#a=(10,20)

#print(a)

#x,y=a
#print(x)
#print(y)

#def calc(a,b):
    #return a+b,a-b,a*b

#t5=calc(7,3)
#packing
#print(t5)

#covert tuple in to list
#l1=list(t5)
#type casting

#print(l1)

#l2=[1,2,3]

#t6=tuple(l2)
#convert from list to tuple

#print(t6)

#t7=(78,34,67,12,8,3,78,34)
#sorted will return list
#result=sorted(t7,reverse=True)
#result= sorted(t7)
#print(result)

#print('length',len(t7))
#print('max ele',max(t7))
#print('sum of ele',sum(t7))

#print('count',t7.count(78))
#print('index',t7.index(34))
#first match ele index

#print('index',t7.index(34,2))


#concat using +

#t1=(1,2,3,4)
#t2=(5,6,7,8)
#t3=(t1+t2)
#print(t3)

#replicate the tuple using *

#t1=(1,2,3,4)

#t1*=3
#print(t1)

#write a python program to createa tuple.
t1=(1,2,3)
print(t1)

t2=()
print(t2)

# wap to create a tuple using different data types
t3=('hello how are you')
print(t3)

t4=(190,140,145,256,789,34,56)
print(t4)

t5=(42,"Hello World!",3.14,True,[9,0,6])
print(t5)

#wap to create a tuple with numbers and print one item.
t6=(22,33,44,55,66,77)
print(t6[3])

#wap to unpack a tuple in several variable.
a=(10,20,30,40,50)
print(a)
p,q,r,s,t=a

print(p)
print(q)
print(r)
print(s)
print(t)

#wap to add an item in several variables.

def calc(a,b,c,d,e,f):
    return a+b+c+d+e+f
t7=calc(7,3,5,6,7,5)
print(t7)

#wap to python program to covert a tuple to a string.
t8=(2,3,4,5,6)
str()
print(str)

#wap to get the 4th element from last of tuple.
t9=("d","h","a","n","u","s")
print (t9[2])

#wap to reverse a tuple.
t10=(79,78,34,65,62,81,90)
result=sorted(t10,reverse=True)
result=sorted(t10)
print(result)

#wap to find the repeated items of a tuple.
t11=(2,4,5,6,3,4,4,7)
print(t11)
count = t11.count(4)
print(count)

#wap to check whether an element exists within a tuple.
t12=(1,2,3,4,5)
result = 9 in t12
print(result)

#wap to convert a list to a tuple.
l1 = [23,43,65,87]
print(l1)
t13 = tuple(l1)
print(t13)

#remove an item from a tuple.
#t14 = ("apple","banana","cherry")
#del (t14[2])
#print(t14)

#wap to slice a tuple.
t15 = (2,4,6,8,10,12,14,16,18)
result = t15[4:12]
print(result)

#index of an item of a tuple.
t16 = (12,13,14,15,16,17)
result = t16.index(15)
print(result)

#to find length of tuple.
t18=(31.32,33,34,35,36)
print('length',len(t18))

#wap to sort list of tuple based on sum.
input:[()]