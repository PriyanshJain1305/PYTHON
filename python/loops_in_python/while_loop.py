#--------------------------------- LOOPS IN PYTHON --------------------------------

#---------------------------------   WHILE LOOPS  --------------------------------
#With the while loop we can execute a set of statements as long as a condition is true.
count = 1
while count <= 5:
    print("hello")
    count += 1

print(count)

#print of numbers with its counting value 
i=1
while i<=6:
    print("priyansh " , i)
    i+=1

print("loop ended")

#reverse print of any number
i=6
while i>=1:
    print(i)
    i-=1

#multiplication table 

# n=int(input("tell me the number : "))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# print elements of list using loop 

"""nums=[1,4,8,9,23,53,245,456,34,6,35,77]
idx=0
while idx<len(nums):
   print(nums[idx])
   idx+=1
#------------------------------------
heroes=["superman","batman", "ironman", "captain america"]
idxx=0
while idxx<len(heroes):
    print(heroes[idxx])
    idxx+=1
"""
#--------------------------     
"""nums=[1,4,8,9,23,53,245,456,34,6,35,77]
x=245
i=0
while i<len(nums):
   if(nums[i]==x):
       print("found",i)
  
   i+=1
"""
# break keyword
# i = 1
# while i < 6:
#   print(i)
#   if (i == 3):
#     break
#   i += 1

#---------------------------------------------------------------
nums=[1,4,8,9,23,53,245,456,34,6,35,77]
x=245
i=0
while i<len(nums):
   if(nums[i]==x):
       print("found at index : ",i)
       break
   else:
       print("finding...")
  
   i+=1

#------------------------------------------------------------------
# continue keyword
#to print even numbers
i = 0 
while i <= 20:
   if(i%2 != 0):
       i+=1
       continue
   print(i)
   i += 1

# to print odd numbers
i = 0 
while i <= 20:
   if(i%2 == 0):
       i+=1
       continue
   print(i)
   i += 1


   
    
