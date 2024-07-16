# ODD EVEN PROGRAM   --------------------------------------------------------
"""oddeven=int(input("tell me the number baby : "))

print("even " if oddeven%2==0 else "odd")"""

# SMALLER AND GREATER NUMBER PROGRAM --------------------------------
"""a = int(input("enter first : "))
b = int(input("enter second : "))
print(a >= b)"""

# --------------------  STRINGS  ------------------------------------------
# (\n) used for line change :::::
# (\t) used for spacing  ::::::
"""str1 = "This is a string. \nWe are creating it in python."
print(str1)
str2 = "This is a string. \tWe are creating it in python."
print(str2)"""

# length of string len()---
"""str3 = "Priyansh"
len1 = len(str3)
print(len1)

str4 = "Jain"
len2 = len(str4)
print(len2)

final_str = str3 + " "+ str4
print (final_str)
print(len(final_str))"""

#indexing in python
str5 = "Priyansh jain"
print(str5 [3])

# importnt (SLICING) str[starting_idx: ending_idx] #ending idx is not included
str = "apna college"
print(str[5:12])

str6 = "apna college"
print(str6[:4]) #[0:4](0 index se given index tk)
print(str6[5:]) # [5: len(str) MEANS ENDING TAK JANA CHAHTE HAI] 

#negative slicing [apple] the indexing start from e which is -1,-2,-3,-4,-5 from right to left

str7 ="apple"
print(str7[-5:-2])

#STRING FUNCTIONS 
# str = "I am a coder."
# str.endsWith("er.") #returns true if string ends with substring
# str.capitalize() #capitalizes the  1st character in a string 
# str.replace( old, new) #replaces all occurrences of old
"""ex: str= 'i am studing python'
       print(str.relace("python","javascript")) 
       output = i am studing javascript"""
# str.find(word) #returns 1st index of 1st occurrer
# str.count("am") #counts the occurrence of substr

agee=int(input("give your age : "))

if(agee>=18):
    if(agee>=80):
        print("cannot drive ")
    else:
        print("can drive")
else:
    print("cannot drive")            


