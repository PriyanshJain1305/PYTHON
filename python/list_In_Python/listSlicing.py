##                       List Slicing
#                   Similar to String Slicing
# list_name [ starting_idx: ending_idx ] # Ending idx is not included


marks = [87, 64, 33, 95, 76]

m1  = marks [ 1: 3 ]        # Ending idx is not included

print ( m1 )                # o/p => [64, 33]

m2 =  marks[ : 4 ]          # is same as marks [ 0 : 4]

print ( m2 )                # o/p => [87, 64, 33, 95]

print ( marks [ 1 : ] )     # is same as marks[ 1 : len(marks) ] And,
                            # o/p => [64, 33, 95, 76]

# marks = [87, 64, 33, 95, 76]
#          -5, -4, -3, -2, -1   idx in -ve 

print ( marks [-3 : -1] )   # o/p => [33, 95] same, Ending idx is not included

P1 = marks [ -2 : len(marks) ]
P1.reverse()
print ( P1 )
# print (marks [ : -3 : -1 ] )
