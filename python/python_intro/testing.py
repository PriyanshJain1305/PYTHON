"""a=int(input("tell me the 1st number : "))
b=int(input("tell me the 2nd number : "))
c=int(input("tell me the 3rd number : "))

if((a>b) and (a>c) ):
    print("a is the largest number")
elif((b>a) and (b>c) ):
    print("b is the largest number")
elif((c>a) and (c>b)):
    print("c is the largest number")"""


numberssrt=[2,25,3,11,54,23,77]
numberssrt.sort()

print(numberssrt)

numberssrt2=[2,25,3,11,54,23,77]
numberssrt2.sort(reverse=True)

print(numberssrt2)