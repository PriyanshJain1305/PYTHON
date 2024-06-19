# rules for variables
# 1. In variable name we can use alphabet(A-Z , a-z) , no.(0-9) and (_)
# 2. in variable name we write no. after variable name not before variable name means (variable1 is valid) (1variable is not valid)
# 3. special character use nahi kar sakte
# 4. variable ka naam kitna bhi bada ho sakta hai

name='priyansh'
age=21
price=29.99
age2=age
print('my name is :' , name)
print('my age is : ' , age)
print('my price is : ' , price)
print(age2)     

#type  (ye variable ka type batata hai ki usme kis type ki value store hai integer , string , float) 

print(type(name))  
print(type(age))   
print(type(price))

# data types int(25, -25, 0) & float(29.99) & string (priyansh by using ("hi" , 'hi' , ''' hi '''))
# boolean (True and False)(T and F must be capital)  ,   None (jisme hum koi value store nahi karte like (a = None (N should be capital)) )

# keywords in python 
# Keyword         	Description
# and --	       A logical operator
# as --       	To create an alias
# assert --	  For debugging
# break	--   To break out of a loop
# class	--   To define a class
# continue	--    To continue to the next iteration of a loop
# def	--   To define a function
# del	--   To delete an object
# elif --	 Used in conditional statements, same as else if
# else --    	Used in conditional statements
# except --	  Used with exceptions, what to do when an exception occurs
# False --	  Boolean value, result of comparison operations
# finally --  Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for	--   To create a for loop
# from --	To import specific parts of a module
# global --	   To declare a global variable
# if --	    To make a conditional statement
# import --	   To import a module
# in --   To check if a value is present in a list, tuple, etc.
# is --   To test if two variables are equal
# lambda -- 	To create an anonymous function
# None	--   Represents a null value
# nonlocal	--    To declare a non-local variable
# not	--   A logical operator
# or	--    A logical operator
# pass	--    A null statement, a statement that will do nothing
# raise --	 To raise an exception
# return --   To exit a function and return a value
# True	--    Boolean value, result of comparison operations
# try	--   To make a try...except statement
# while	--     To create a while loop
# with	--    Used to simplify exception handling
# yield	--   To return a list of values from a generator

#addition 
a=200
b=300
sumsub=(a+b  , a-b)
print("result of addition and substraction = " , sumsub)

#expression execution in python 
# it means that 1. string and numeric values can operate together with (*)
  
p,b=2,3
text="@"
print(2*text*3)

#string and string can operate with (+)
A,C="4",5
txt="@"
print((A+txt)*C)

#floor = it gives a closest integer , which is lesser or equal to the float value.
# (integer deivison = //) iska matlab divide hi hota hai ye output se uski approximate choti value dega ex.(5.6 aaya to ye use 5 dega)

R , Q = 12 , 5
D = R // Q
print(D)

# if we are finding remainder some conditions are if (numerator is + and denominatore is + the result will be + )
# n= (-) d=(-) result (+)            n= (+) d=(-) result (-)         n= (-) d=(+) result (+) 

B , V = 5 , -2
W = b % V
print(W)

# Taking INPUT from user

""" Name=input("name is  ")
AGE=int(input("and my age is"))
PRICE=float(input("PRICE "))
print("my name is " , Name , "and my age is " , AGE   )
print(PRICE) """

#CONDITIONAL STATEMENT

"""LIGHT=input("color of light : ")
if(LIGHT == "red"):
    print("stop")
elif(LIGHT == "yellow"):
    print("wait") 
elif(LIGHT == "green"):
    print("go")
else:
    print("light is broken ")"""        

    #turnary operator we can write conditional statement in one line

"""Food=input("tell me the food name : ")
eat= "yes" if Food=="cake" else "no"
print(eat)"""

"""Food=input("tell me the food name : ")
print("sweet" if Food=="gulab jammon" or Food=="rasmalai" else "not a sweet dish")
"""

#one more conditional statement known as clever if

"""umar=int(input("umar batao : ")) 
vote=("yes","no")  [umar<18]
print(vote)"""

"""sal=float(input("salary : " )) 
tax=sal*(0.1, 0.2) [sal>50000]
print(tax)  
"""
p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))
si = (p*r*t)/100
print(si)

