##                     Lists in Python
# A built-in data type that stores set of values
# It can store elements of different types ( integer, float, string, etc. )

marks = [87, 64, 33.11, 95, 76]            #marks[0], marks[1]..

print ( marks [0] )
print ( marks [2] )
print ( marks [1] )
print ( marks [4] )
print ( marks [3] )

print ( type ( marks) )          # O/p =>  <class 'list'>

print ( "Length of marks :", len ( marks ) )    # O/p => Length of marks : 5

student = ["Karan", 85, "Delhi"]

print ( student [ 2 ] )          # O/p => Delhi


## note 👇
# stringe  →   immutable  ( mtlb not changeable )
# lists    →   mutable    ( mtlb changeable )

# student = ["Karan", 85, "Delhi"]

student [ 0 ] = "harsh"     # 0 indexing change kar di student ki yeh list mai ho sakta hai mtlb hum kar sakte hai
student [ 2 ] = "indore"
print ( student )


