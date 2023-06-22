# Program to get the maximum value from input
# Explain: map() function returns a list of results after applying the given function to each item of a given iterable (list, tuple etc.)
# map(function, iterable, ...)
# function : It is a function to which map passes each element of given iterable.
# iterable : It is a iterable which is to be mapped.
# Returns a list of the results after applying the given function  
# to each item of a given iterable (list, tuple etc.)
x,y,z=map(int,input("Enter three numbers separate with space: ").split(' '))
print("Maximum value is: ",max(x,y,z))

# Another way
# x,y,z=map(eval,input("Enter three numbers separate with space: ").split(' '))
# print("Maximum value is: ",max(x,y,z))