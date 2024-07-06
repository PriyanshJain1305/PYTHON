# WAP to ask the user to Enter names of their 3 favorite game store them in a list.


"""games = []

games.append ( str ( input ("Enter frist Game  :" ) ) )
games.append ( str ( input ("Enter Second Game :" ) ) )
games.append ( str ( input ("Enter Third Game  :" ) ) )

print ( games )
"""

#-------------------------------------------------------------------------------------#


# WAP to check if a list contains a palindrome of elements. ( Hint: use copy() method )


list1 = [1, 2, 2, 1]

copied_list1 = list1.copy()
copied_list1.reverse()

if ( copied_list1 == list1 ):

    print ("List is a palindrome")

else: 

    print ("List is not a palindrome")

    #------------------------------------------------------------------------#

list1 = ["m", "a", "a", "m", "p"]
copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):

    print("palindrome")

else:

    print("NOT palindrome")
