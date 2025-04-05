# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 13:58:19 2025

@author: HP
"""



#to print following output.

#number of rows:5
#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1 

#n= int(input("number of rows:"))
#for i in range(n):
    #for j in range(n-i):
        #print(j+1,end=" ")
    #print()


#to print number pattern.
#1 1 1 1 1 
#2 2 2 2 
#3 3 3 
#4 4 
#5 
#n= int(input("number of rows:"))
#for i in range(n):
    #for j in range(n-i):
        #print(i+1,end=" ")
    #print()
    
    
#print the following pattern.
#number of rows:5
#5 5 5 5 5 
#4 4 4 4 
#3 3 3 
#2 2 
#1 

#n= int(input("number of rows:"))
#for i in range(n):
    #for j in range(n-i):
        #print(n-i,end=" ")
    #print()



#number of rows:9
#9 8 7 6 5 4 3 2 1 
#9 8 7 6 5 4 3 2 
#9 8 7 6 5 4 3 
#9 8 7 6 5 4 
#9 8 7 6 5 
#9 8 7 6 
#9 8 7 
#9 8 
#9 

#n= int(input("number of rows:"))
#for i in range(n):
    #for j in range(n-i):
        #print(n-j,end=" ")
    #print()

#number of rows:7
#7 6 5 4 3 2 1 
#6 5 4 3 2 1 
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1 
#n= int(input("number of rows:"))
#for i in range(n):
    #for j in range(n-i-1,-1,-1):
        #print(j+1,end=" ")
    #print()



#n= int(input("number of rows:"))
#for i in range(n):
    #for j in range(n-i-1,-1,-1):
        #print(n-j,end=" ")
    #print()
    
    
# Python program that counts the occurence of vowels and consonants in a given str.

def count_vowels_and_consonants (text):
    """
    counts  the occurence of vowels and consonants in a string.

    Args:
        text : The input string.
        
    Returns:
        A tuple containing the number of vowels and consonants.
    """
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count

text = "Hello, Akola!"
vowel_count, consonant_count = count_vowels_and_consonants(text)
print(f"Vowels: {vowel_count}")
print(f"Consonants:{consonant_count}")

    












#to print the pattern

#1 2 3 4 
#1 2 3 4 
#1 2 3 4 
#1 2 3 4 
#1 2 3 4

#n= int(input("number of rows:"))
#for i in range(n):
    #for j in range(n-1):
        #print(j+1,end=" ")
    #print()