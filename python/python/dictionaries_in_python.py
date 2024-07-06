#------------------------------# Dictionary in Python #-------------------------------#

# Dictionaries are used to store data values in key : value pairs
# They are unordered, mutable(changeable) & don’t allow duplicate keys

dict = {

"name" : "shradha",
"'cgpa" : 9.6,
"marks" : [98, 97, 95],
"friends" : ["shubham", "saurabh", "rahul"]

}

# print ( dict )                # O/p => {'name': 'shradha', "'cgpa": 9.6, 'marks': [98, 97, 95], 'friends': ['shubham', 'saurabh', 'rahul']}
# print ( type ( dict ) )       # O/p => <class 'dict'>

# print ( dict ["name"] )       # O/p => shradha  yeh key ki value ko print karta hai
# print ( dict ["friends"] )    # O/p => ['shubham', 'saurabh', 'rahul']

## Abh mai "name" key ki value change karunga 

dict ["name"] = "janmesh"
# print (dict ["name"] )  

## Abh new key add karunga Dictiionary mai

dict ["SurName"] = "thakur"   # last mai SurName key add ho gyi or uski value bhi 
# print ( dict )


#---------------------------------------------------------------#

dict2 = {}                  # yeh null dictionary hum iske ander key : value daal sathte hai or print bhi kar sakte hai 

# print (dict2)

## Add new key and value in null dict2 

dict2 ["NAME"] = "somesh"   
dict2 ["day"]  = "new "         
# print ( dict2 )           # O/p => {'NAME': 'somesh', 'day': 'new '}


#--------------------------------# Nested dictionary #----------------------------------#


student = {

"name" : "rahul kumar",
"subjects" : {

            "phy"  : 97,
            "chem" : 98,
            "math" : 95

},
"clg" : "mit"

}

#nested dictionary

print ( student )           # O/p => {'name': 'rahul kumar', 'subjects': {'phy': 97, 'chem': 98, 'math': 95}, 'clg': 'mit'}

print ( student [ "subjects" ] )        # O/p => {'phy': 97, 'chem': 98, 'math': 95}
