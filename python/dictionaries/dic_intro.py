#------------------------------# Dictionary in Python #-------------------------------#

# Dictionaries are used to store data values in key : value pairs
# They are unordered, mutable(changeable) & don’t allow duplicate keys

dict = {

"name" : "priyansh",
"'cgpa" : 7.6,
"marks" : [78, 77, 75],
"friends" : ["parv", "janmesh", "amratansh"]

}

# print ( dict )     ---------- # O/p => {'name': 'Priyansh', "'cgpa": 7.6, 'marks': [78, 77, 75], 'friends': ['Parv', 'amratansh', 'janmesh']}
# print ( type ( dict ) ) ----- # O/p => <class 'dict'>

# print ( dict ["name"] ) ------ # O/p => shradha  yeh key ki value ko print karta hai
# print ( dict ["friends"] ) ---- # O/p => ['Parv', 'amratansh', 'janmesh']

## Abh mai "name" key ki value change karunga 

dict ["name"] = "Priyansh"
# print (dict ["name"] )  

## Abh new key add karunga Dictiionary mai

dict ["SurName"] = "Jain"   # last mai SurName key add ho gyi or uski value bhi 
# print ( dict )


#---------------------------------------------------------------#

dict2 = {}                  # yeh null dictionary hum iske ander key : value daal sathte hai or print bhi kar sakte hai 

# print (dict2)

## Add new key and value in null dict2 

dict2 ["NAME"] = "PARV"   
dict2 ["day"]  = "new "         
# print ( dict2 )           # O/p => {'NAME': 'Parv', 'day': 'new '}


#--------------------------------# Nested dictionary #----------------------------------#


student = {

"name" : "Priyansh jain",
"subjects" : {

            "phy"  : 97,
            "chem" : 98,
            "math" : 95

},
"clg" : "mit"

}
student.update =({"city" : "delhi"})
#nested dictionary

print ( student )           # O/p => {'name': 'Priyansh jain', 'subjects': {'phy': 97, 'chem': 98, 'math': 95}, 'clg': 'mit'}

print ( student [ "subjects" ] )        # O/p => {'phy': 97, 'chem': 98, 'math': 95}

#-----------------NESTED DICTIONARY (dictionary ke ander dictionary banana )

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#print(myfamily)
print(myfamily["child1"]["name"])


