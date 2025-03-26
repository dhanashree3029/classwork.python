# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#all arithmetic operations using two numbers.
#num1 =10
#num2 =20
#sum = num1 + num2

#print(sum)
#print (10 + 20)
#print(20 - 15)
#print(5 * 7)
#print(50 / 10)
#print(40 % 15)


#wap to find area of triangle.
#b=float(input('Enter the base of triangle'))
#h=float(input('Enter the height of triangle'))
#a=1/2*b*h
#print('The area is',a)

#wap to find greatest of two numbers.
#num1 = int(input("Enter first numbers :"))
#num2 = int(input("Enter second number :"))
#if num1 > num2:
   # print(num1,"is greater")
#else:
   # print(num,"is greater")
   
   
#WAP to find square and cube of two numbers.
#n=float(input('Enter the number'))
#s=n**2
#c=n**3
#print('Square=',s)
#print('Cube=',c)


#Swap two variables
#x=8
#y=9
#print(x,y)
#x,y=y,x
#print(x,y)

#wap to find simple interest
#p=float(input('Enter the principle'))
#r=float(input('Enter the rate of interest in percentage'))
#t=float(input('Enter the time'))
#s=p*r*t/100
#print('simple interest=',s)


#wap to enter marks of five subjects and calculate total, average and percentage
#a=int(input('Enter the marks of first subject'))
#b=int(input('Enter the marks of second subject'))
#c=int(input('Enter the marks of third subject'))
#d=int(input('Enter the marks of fourth subject'))
#e=int(input('Enter the marks of fifth subject'))
#t=a+b+c+d+e
#p=t/500*100
#print('Total=',t)
#print('Percentage=',p)


# print 1- 20 & sum of numbers

#a=1
#sum=0
#while a<=20:
   #print(a)
    #sum=a+sum
    #a+=1
    
#print('sum is',sum)


#num1= 121
#num2= 229
#while num1<=num2:
     # if num1 % 2 == 0: 
          # print(num1)
      #num1+=1
       
      
#num1= 521
#num2= 229
#while num1>=num2:
    #if num1 % 2 != 0:
       # print(num1)
    #num1-=1
    
    
# to check it is armstrong or not
#num = int(input("Enter a number :"))

# initialize sum
#sum = 0

#find the sum of the cube of each digit
#temp = num
#while temp > 0:
    #digit = temp % 10
    #sum += digit ** 3
    #temp //= 10
    
    # display the result
   # if num == sum:
      #  print(num,"is an Armstrong number")
  #  else:
       # print(num,"is not an armstrong number")
    
    
# palindrome 
#n = int(input(("Enter number:")))
#temp = n
#r = 0
#while n > 0:
    #d = n % 10
    #d = r * 10 + d
    #n = n // 10
   # if temp == r:
       #print("Palindrome")
    #else:
        #print("Not Palindrome")

#wap to print squares from 1 to 20.
#i=1

#while i<=20:
   #print (i*i)
   #i+=1
   
   #wap to print table of given number.
#i=1
#n=2
#while i<=10:
     #print (n,"*",i, "=",n*i)
     #i=i+1
     
     
#wap to count number of digits in a number
#num = 1234
#count = 0

#while num != 0:
   # num //=10
   # count += 1
#print("number of digits :" , count)
  

#fibonacii series.
#num = int (input("Enter a number:"))
#print("Fibonacii series :")
#num1 = 0
#num2 = 1
#count = 0
#print(num1,end=" ")
#print(num2,end=" ")
#while count < num:
    #result = num1 + num2
    #print(result,end=" ")
    #num1 = num2
    #num2 = result
    #count = count + 1
    
#wap to print sum of all even numbers from 1 to n.
#n= int(input("Enter a number :"))
#for i in range (1, n+1):
    #if i%2==0:
        #print (i)
        
#wap to print all odd numbers from 1 to n.
#n= int(input("Enter a number"))
#for num in range (1, n+1):
    #if num % 2 != 0:
        #print(num)

#wap to check whether it is prime or not.
#n=int(input("Enter a number"))
#i=2
#temp=0
#while i<n:
    #if(n%i==0):
        #temp=1
        #break
   # i+=1
    
    #if temp==0:
        #print('prime no')
    #else:
        #print('not prime')
        
        
#wap to print even numbers from 121 to 229 usi for loop
#for x in range(121,229,1):
    #print(x)
    
#wap to print odd nos from 521 to 229.
#for x in range(521,229,-2):
    #print(x)

#wap to print all alphabets.
#for a in range(97,127):
   # print(chr(a),a)
    
#wap to find sum of all even numbers between 1 to n
#n= int(input("enter a number"))

#for i in range(2,n+1,2):
    #print(i)
 
#wap to find sum of all odd nos.bteween 1 to n.
#n= int(input("enter a number"))

#for i in range(1,n+1,2):
    #print(i)
    
#to find sum of all odd numbers between 1 to n
#n= int(input('enter number:'))
#s=0
#for i in range (1,n+1,2):
    #s+=i
#print('sum=',s)
 
    
    
#row=1   
#while row<=5:
     #col=1
     #while col<=5:
         #print('*',end="")
         #col+=1
     #print()
     #row+=1
     
#Print* using for in loop
#n = int(input("enter a number:"))

#i = 1

#while(i<=n):
    #j = 1
    #while(j<=1):
        #print("*",end=" ")
        #j+=1
    #print()
    #i+=1

#print* pattern in python using for loop
# *
# * *
# * * *
# * * * * 
# * * * * *
#for j in range(1,6):
    #for i in range(0,j):
        #print("*",end=" ")
    #print(" ")
    
#Wap to print
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

#n = int(input("Enter a number of rows:")) 
#for i in range (1,n+1):
    #for j in range(1,i+1):
        #print (j,end="")
    #print (" ")
     
#wap using while loop * pattern.
#row = 0
#while row<5:
    #star = row+1
    #while star>0:
        #print("*",end=" ")
        #star=star-1
    #row = row+1
    #print()
    
#wap* pattern program.
#for j in range(6,1,-1):
    #for i in range(0,j):
        #print("*",end=" ")
    #print(" ")
    
#wap to print
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
 
#n = int(input("Enter a number of rows:"))
#num = 1
#for row in range (1,n+1):
    #for col in range(1,row+1):
        #print(num,end=" ")
        #num=num+1
    #print()
    
    
    
#n = int(input("Enter a number of rows:"))
#for i in range (1,n+1,):
    #for j in range(1,i+1):
       #print(j,end=" ")
    #print ( )
    
#for i in range(1,6):
   # for j in range(i,0,-1):
        #print(j,end="")
    #print()
    
    
#n1=3+23

#n2=2+4j
    
#print(n1)
#print(n2)
#print(type(n1))
#print(n1.real)
#print(n1.imag)
       
#n3=n1+n2
#n4=n1-n2

#print(n3)
#print(n4)


#wap * and / of complex nos.
#n1=5+6j

#n2=7+4j

#n3=n1/n2

#print(n3)

#wap multiplication
#n1=6+7j

#n2=5+7j

#n3=n1*n2

#print(n3)

# wap division of complex nos.
#n1=6+7j

#n2=5+7j

#n3=n1/n2

#print(n3)
  
 #wap usinf for loop
#n=5:
#for i in range (n):
    #for j in range(i+1):
        #for j in range(1,i=j):
            #print(j,end='')
            
        #for j in range(i-1,0,-1):
            #print(j,end='')
        #print()
#rows=1
#columns=4
#print_pattern(rows)
#print_pattern(columns)


#a=10
#b=11
#c=12
#print(id(a))
#print(id(b))
#print(id(c))
#print(a is b)
#print(b is c)
    

#s1='single line'
##s2="It's a car"

#s3=''' this is for
      # multiple line'''
       
#print(s1)
#print(s2)
#print(s3)
     

#s1='Hello'

#print(s1)

#for i in s1:
    #print(i)
    
#print(s1[1])
     
   
#s1="Helloworld"   
  
#to find no. of character in the string.(len)
#print(len(s1))

#s1="Hello world Hello Hello"

#print(s1.lower())
#s2=(s1.lower())
    

#replace
#s1=s1.replace("Hello","Hi",2)
#print(s1)

# find() gives the start index of that word
#second parameter inform that ,start searching the word.
#from given index.
#index param is optional.
#if not provided,so finf will return first match.
#print(s1.find("Hello"))
#int(s1.find("Hello",15))

#find the frequency
#if we provide the second param
#start counting the given word from the text.
#print(s1.count('Hello',5))

# string is immutable.

#s1="Hello"

#id is gget the memory location.
#print(id(s1))
#print(s1)

#s1=s1+" world"

#print(s1)
#print(id(s1))

#is digit()

#s1='Amol'

#print(type(s1))
#is if the given str contains only numbers
#isdigit()will return true else it returns false

#print(s1.isdigit())
#if given string contains only nos.
#else return false.
#print(s1.isalpha())

#if str contains only space
#print(s1.isspace())

#slice the given string.
#s1="hello to python"

#print(s1)

#print(s1[0])

#print(s1[0:5])

# to get the word reverse order
#print(s1[5:0:-1])

#print(s1[14:1:-3])

#print(s1[0:15:2])

#print(s1[-1:-11:-1])

#print(s1[::-1])

#string pallindrome
#str1='nitin'

#str2=str1[::-1]

#if str1==str2:
    #print('string is pallindrome')
#else:
    #print('not pallindrome')


# 1.python program to remove given charater from string.

#replace

#s1 = "Hello world"
#s = s.replace("l","")
#print(s)

#2. to count occurences of given character in string.
#print(s1.count('Hello',5))
#print(s1.count('l'))

# 3. to check string is pallindrome or not.
#str1='pratik'

#str2=str1[::-1]

#if str1==str2:
    #print('string is pallindrome')
#else:
    #print('not pallindrome')
    
    
    
# 4. to check given character is vovel or consonant.

#ch = input("Enter the Alphabet : ")
 
#if ch in ('a','e','i','o','u','A','E','I','O','U'):
    #print(ch,"is a vowel")
#else:
    #print(ch,"is a consonant") 
    
    
# 5.python program to check given character is digit or not.

#character = input("Enter a character: ") 

#if character.isdigit():
    #print("The character is digit.")
#else:
    #print("The character is not digit.")
    
    
# 6. python program to check given character is digit or not using isdigit() 
 
#string = input("Enter a string: ")

#if string.isdigit():
    #print("The string is digit.") 
#else:
    #print("The string is not digit.")
    
    
# 7. replace the string space with a given character

#str= "Python"
#print(str.replace("t","h"))

 # 8.python program to replace the string using replace method.

#str = "Harry potter" 
#print(str.replace("r","p")) 
     
    
# 9.to convert lowercase char to uppercase of string.
#string = "hello"
#print(string.upper())
    
    
 # 10.covert lowercase vowel to uppercase in string.

#s = input("Enter a string :")
#res = "aeiou"
#for i in s:
    #if i in res:
        #upr = i.upper()
    #s = s.replace(i, upr)
#print("after converting:",s)
    
    
 # 11.python programs to delete vowels in a given string.

#string= input("Enter a string: ")

#vowels= "aeiouAEIOU" 

#result = ""

#for character in string:
    #if character not in vowels:
        #result += character
#print(result)
    
    
 # 12.python program to count alphabet, digit and special character.
#input_str = input("Enter a string: ")   
#alphabet_count = 0
#digit_count = 0
#special_char_count = 0

#for char in input_str:
    #if char.isalpha():
        #alphabet_count += 1
    #elif char.isdigit():
        #digit_count += 1
    #elif not char.isspace():
        #special_char_count += 1

#print("Alphabet count:", alphabet_count)
#print("Digit Count:", digit_count)
#print("Special Character Count:", special_char_count)
    

 #python program to separate characters in agiven string.
#input_str = input("Enter a string: ")
  
#print("Original string:", input_str)
#print("separated characters:")
#for char in input_str:
      #print(char)
      
#wap to replace every character by its next character.
#s = input("Enter a string:")
#s1=""
#for i in range(0, len(s)):
    #if s[i]==" ":
           #s1+="-"
    #else:
            #s1+=s[i]
    #print("converted string is:")
    #print(s1)
# definition of function

#def addition():
    #a= int(input('enter a number '))
    #b= int(input('enter a number '))
    #c=a+b
    #print(c)

#create function to perform add.
#def addition(a,b):
    #c=a+b
    #return c

#sum=addition(10,20)
#print(sum)


#def multiplication(a,b):
    
 #a = int(input("Enter first num: "))
 #b= int(input("Enter second num: "))
 #c=a*b
 #return c
 #print("multiplication", c)

#def division(e,f):
    #c=e/f
    #return c

#division=(35/7)
#print(division)

#square 

#def square (number):
    #return number * number

#number = 9
#result = square (number)
#print(result)

# Return multiple values in python.

#def calculation(a,b):
    #c=a+b
    #d=a*b
    #z=a-b
    #return c,d,z

#a=int(input('enter a number'))
#b=int(input('enter a number'))
#sum,mul,sub=calculation(a,b)
#print(f'addition is {sum}')
#print(f'mul is{mul}')
#print(f'sub is{sub}')


#wap to create a function that takes two arguments, name and age, and print their values.
#def display(name,age):
 #print(f'Hello{name},and{age} age')
 #display('Dhanashri',25)
 
#wap to create function calculation () such that it can accept two variablesand calculate addition and subtraction.alsonit must retur both addition and subtraction in a single cell.

#def calculation(a,b):
    #c=a+b
    #d=a-b
    #return c,d

#a=int(input('enter a number'))
#b=int(input('enter a number'))
#sum,sub=calculation(a,b)
#print(f'addition is{sum}')
#print(f'sub is{sub}')

#wap to create function show employee() using the following conditions.
#it should accept the employee's name and salary accept the both.
# if the salary is missing the function call then assign default values 9000 to salary.

#def showEmployee(name,salary=9000):
    #print("Employee Name:",name)
    #print("Employee Salary:",salary)
    
#showEmployee("sia",9000)


        

#create a function to accept a number and its factorial.

#def factorial(no):
    #if no==0 or no==1:
        #return 1
    #else:
        #return no*factorial(no-1)
#result=factorial(5)
#print(result)


#create a function to generate fibonacii series like 0,1,1,2,3,5

#num = int(input("Enter a number :"))
#def fibonacii (num):
    #if num==0:
        #return 0
    #elif num == 1:
        #return 1
    #else:
        #return fibonacii(num-1) + fibonacii(num-2)
#for i in range(num):
    #print(fibonacii(i),end=" ")
    
#create a menu driven calculation (add,sub, multiply,divide, mod) using function.
#x=int(input("Enter first number:"))
#y=int(input("Enter second number:"))
#a=x+y
#b=x-y
#c=x*y
#d=x/y
#print("Addition=",a)
#print("Subtraction=",b)
#print("Multiplication=",c)
#print("Division=",d)


# create a function to accept a student data, calculate the total & percentage,
#return total and percentage.

#def calculate_student_data():
  # """calculate & prints student total marks and percentage."""
  
  
#name = input("Enter Student name:")
#subject_1_marks = float (input("enter marks of subject 1:"))
#subject_2_marks = float(input("enter marks of subject 2:"))
#subject_3_marks = float(input("enter marks of subject 3:"))
#marks_obtained =float(input("enter marks obtained of subject"))
 
#total_marks= subject_1_marks + subject_2_marks + subject_3_marks
#percentage = (marks_obtained/300)*100


#print("\n....student data.......")
#print(f"name:{name}")
#print(f"Total marks :{total_marks}")
#print(f"percentage: {percentage:.2f}%")

#calculate_student_data()

# Create a login function , that accept username & password, if username is 
# 'admin' & password is 'admin@123

#count = 0
#while count < 3:

    #username = input("Enter username:")
    #password = input("Enter password:")
#if username =='admin' and password =='admin@123':
        #print('true')
        #break
        
#else:
        #print('False')
        #count+=1
        
# create a function which accept string character, check the occurences of given char.
        
        
#my_string = input("Enter a string:")
#my_char = input("enter a character:")

#freq = 0
#for letter in my_string:
    #if letter == my_char:
        #freq += 1
#print("character has occured %d times" % freq)



#wap is_prime()function.
#def is_prime(number):
    #if number > 1:
        #for i in range(2, number):
            #if(number % i) == 0:
                #return False
            #return True
    #else:
        #return False
    
    #number =  int(input("Enter a number to check:" ))
    
    #if is_prime(number):
        #print(f"{number} is a prime number.")

    #else:
        #print(f"{number} is not a prime number.")
        
        
        
        
        
#create list of cities & display it using for in lopp.

list1=['Pune','Nagpur','Akola','Thane']
# check the type
print(type(list1))
for i in list1:
    
    list1[3]="washim"
    print(i)
    print(list1)




