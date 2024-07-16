#-----------------------FOR LOOPS---------------------------

# for loop is used to iterate over a sequence (list, tuple, string) or other iterable
nums=[ 1 , 2 , 3 , 4 , 5 ]
veggies=["banana","potato","tomato"]
for val in nums , veggies:
    print(val)
else:
    print("done")

#-------------------Looping Through a String-------------
str="priyansh"
for x in str:
  print(x) 
print("------------------------------")  

#--------------------BREAK STATEMENT---------------------------------    
str="priyansh"
for x in str:
  if(x=='a'):
     print(" a found ")
     break
  print(x) 
print("end")

#-----------------------------------------------------
print("1, 4, 9, 16, 25, 36, 49, 64, 81, 100")
X = int ( input ("Enter number, which one want to find in tuple : "))

num3 = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
c = False

for i3 in num3:
    if ( i3  == X ):
        print ( "Number is found in tuple" )
        c = True
        break

if ( c == False ):
    print ( "Number is not found in tuple") 


#----------------NESTED FOR LOOP --------------------------------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    