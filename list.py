# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 11:53:50 2025

@author: HP
"""

#functions of list
#list1=[23,67,12,8,36,77,67,23,67]

#print(list1)

#add the element at the last in the list
#list1.append(91)
#print(list1)

#insert the element using index
# index,value
#list1.insert(3,55)
#print(list1)

#remove element using index
#list1.pop(2)
#print(list1)

#to get frequency of element in the list
#print('count of element',list1.count(67))

#get the list count
#print('total elements',len(list1))
#print('max element',max(list1))
#print('minimum element',min(list1))
#print('sum of elements',sum(list1))

#sort in asc order
#list1.sort()

#sort using desc order
#list1.sort(reverse=True)
#list1.reverse()
#print(list1)

#list
#student = ["siya",67,23,"Delhi"]
#print(student)

#wap to ask the user to enter names of ttheir 3 favourite movies & store them in a list
#movies =[]
#mov1 = input("Enter 1st movie: ")
#mov2 = input("Enter 2nd movie: ")
#mov3 = input("Enter 3rd movie: ")

#movies.append(mov1)
#movies.append(mov2)
#movies.append(mov3)

#print(movies)



#list1 = [1, 2, 1]
#list2 = [1, 2, 3]

#copy_list1 =[1, 2, 1]
#copy_list1.reverse()

#if(copy_list1==list(1)):
    #print("palindrome")
#else:
    #print("Not pallindrome")
    
    
    
    
#list1 =[10,20,30,40,50,60,70,80,90,100]

#slicing
#list2=list1[3:9:2]

#print(list2)

#list3=list1[-2:-8:-2]
#print(list3)


# +concat & *replication

#l1,l2=[1,2,3,],[5,6,7]

#l3=l1+l2
#print(l3)

#l4=[2,4,6]
#l4*=3

#print(l4)

#membership operator in, not in

#in-->check element is present in the collection or not
#element is present then return true else return false

# not in-->if element is not present then return true
#else return false
#result=3 not in l1
#print (result)

#if  3 not in l1:
    #l1.append(3)
    
    
#wap to remove to find duplicate element in list
#l1=[1,2,2,3,4,4,5]
#list =[]
#for val double in l1:
    #if val not in l1:
        #l1.append(val)
    #else val not in l1
#print(l1)

#wap to sort the given list
#list1 = [23,45,76,89,98,77,87]
#list1.sort()
#print(list1)

#to get largest no. from list.

#print('max element',max(list1))


#to count the no of string where the string length is 2


#list1=['aba','121','kg','ab']
#string = input("Enter string:") 
#c = input("enter acharacter to count:")
#count = 0
#for char in string:
    #if c == len:
        #len += 2
#print(c," ",count)




#wap to find the list of  words that are longer than given words
#string = input("Enter a string:")


#wapto crete even and odd list
#list[2,1,42,57,35,36,9,3]
#for i in list:
    #if(i%2==0):
          #print(i," is even")
    #else:
          #print(i," is odd")
          
          
#wap functions that takes two lists and returns True if they have atleast one commom member.
#list1 = [1,2,3,4,5,6]
#list2 = [7,8,9,2,10]
#for x in list1:
    #for y in list2:
        #if x==y:
            #print("Common element is: ",x)
            
            
#wap to print specified list after removing the oth,4th,and 5th element go to the edior

#list1=['red', 'green','yellow','pink', 'blue',]
            
#list2=[list1[1:4:1]]
#print(list2) 

#create alist of elements & find the freq of each element in the list.

#list =input("enter a list:")
#num = input("enter a number:") 

#freq=0
#for numbers in  list:
    #if numbers == num:
        #freq += 1
#print("num has occured %d times" % freq)



#list1=[10,20,30,40,10,40,40]
#counted=[]
#for i in range(len(list1)):
    #if list[i] not in counted:
        #count = 0
        #for j in range(len(list1)):
            #if list1[i] ==list1[j]:
                #count += 1
            #print(f"{list1[i]}: {count}")
            #counted.append(list1[i])
            
            
list1=[1,2,3]

#syntax
#
#[expression for item in collection if condition]

#result= [5*i for i in list1]

#print(result)

#result2=[i*i for i in list1]
#print(result2)

#list2=[45,78,99,12,55]

#get only even numbers from the list.

#result3=[i for i in list2 if i%2==0]
        
#print(result3)

#for i in list2:
    #if i%2==0:
        #print(i)
        
        
 #wap print square of 1 to 20 nos. using comprehension.

#squares =[x**2 for x in range(1,21)]
#print(squares)


#wap to print values if value is <100.

#i =[i in range (1,99), i+=1]
#print(i)
        

        

#create 3*3 matrix to perform addition of given matrix.
#m1=[[1,2,3][10,20,30][4,5,6]]
#m2=[9,8,7][6,5,4][3,2,1]

#result =[m1[i][j]+m2[i][j] for j in
#range(len(m1[0]))] for i in
#range(len(a))]

#for add in result:
    
    #print(add)