#---------------------- RANGE IN FOR LOOP IN PYTHON ----------------


 # range( start?, stop, step?)
 # start? - optional, default is 0
 # stop - required, WHERE TO STOP
 # step - optional, KITTE SE GAP SE BADNA HAI


 # for i in range ( 5 ):             # first way to print, using "range" function
 #     print ( i )


 # for i2 in range ( 3, 9 ):         # Second Way to print, using "range" function  
 #     print ( i2 )


 # for i3 in range ( 3, 10 , 3 ):    # third and best way to print, using "range" function
 #     print ( i3 )
# #---------------------------------------------------------------------------------------------------#
# ## print Odd number 1 to 20 using " range " 


# # range( start?, stop, step? )
# for i4 in range ( 1, 20, 2 ):
#     print ( i4 )


# #---------------------------------------------------------------------------------------------------#
# ## print Even number 1 to 20 using " range " function


# # range( start?, stop, step? )
# for i5 in range (2, 21, 2 ):
#     print ( i5 )
#---------------------------------------------------------------------------------------------------#

#REVERSE COUNTING ----------------
for i6 in range ( 1000, 200, -10 ):
     print ( i6 )
#---------------------------------------------------------------------
a = int ( input ("Enter number for table : ") )
for i7 in range ( 1, 11 ):
     print ( a ,"*" , i7, "=" , i7 )

#---------------------------------------------------------------------
# sum of n numbers ------------------
# through while loop ----------------
a1 = int ( input ("Enter number : ") )

i = 0
sum = 0
while ( i <= a1 ):
     sum += i
     i += 1

print ( a1, "number tak ka sum : ", sum  )

# throgh for loop -------------------------
n=int(input("tell no. : "))
i=0
sum=0
for i in range(i , n+1):
    sum += i
    i += 1
print(   "total sum = " , sum)

#-------------factorial program----------------------
# using while loop-----------------------------------

n=3
f=1
i=1
while (i<=n):
    f*=i
    i+=1

print("fact" , f)

#-------------------------------------------------------------------------
#using for loop 
n = int(input("Enter a number: "))

factorial = 1

if n < 0: #Check if the number is negative
   print("Factors do not exist for negative numbers.")
elif n == 0: #Check if the number is zero
   print("The factorial of 0 is 1.")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial of",n,"is",factorial)

   #-------------------------------------------------------------------
#             prime number program 
# number=int(input("tell me the number : "))   
number=int(input("tell me the number : "))   
i=0
if (number==1):
   print("number is prime:")

for i in range(2,number):
   if (number%i==0):
      print("number is not prime:")
      break
else:
      print("number is prime:")
 

 
   
