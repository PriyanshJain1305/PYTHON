# ------------------------------methods in dictionary--------------------------------------------

# METHODS               DESCRIPTION
# clear()     	Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()    Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()      	Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()    	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary   

#----------------------------------------------------------
#                          REMOVES ITEM () METHOD


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")  #The pop() method removes the item with the specified key name:
print(thisdict)

#------------------------------------------------------------------------

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()    #The popitem() method removes the last inserted item
print(thisdict)

# -------------------------------------------------------------

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]  
print(thisdict)

#The del keyword removes the item with the specified key name:
#The del keyword can also delete the dictionary completely:

#--------------------------------------------------------------------
#  ----------------------  UPDATE DICTIONARIES () METHOD
student = {
"name" : "Priyansh jain",
"subjects" : {
                "phy"  : 97,
                "chem" : 98,
                "math" : 95

}
}
student.update({"city" : "delhi"})
print(student)

#-----------------------------------------------------------------------
#  ---------------------- TO PRINT ONLY VALUES IN DICTIONARIES () METHOD

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)
