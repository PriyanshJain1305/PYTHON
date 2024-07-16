# a=(input("tell me the sting  : "))
# if(a==a[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")
#---------------------------------------------------------------------
#palindrome program without using function

b=int(input("tell "))
a=0
while(b>0):
    a=a*10
    c=b%10
    a=a+c
    b=b//10

if(b==a):
    print("palindrome")
else:
    print("not palindrome")
print(a)
print(b)    