# Creating function in Python
def a_function():
    print("You Just Created a function")
a_function() 

#Empty Function
def empty_function():
    pass
print(empty_function())

#Add function to create
def add(a,b):
    return a+b
print(add(2,3))
# args and **kwargs to take infinite no of arguments and keyword respectivley
def many(*args, **kwargs):
    print(args)
    print(kwargs)
many(1,2,3, name="Mike", job="programmer",names="Name")
#Defining Global to access variable outside of scope of function
def function_a():
    global a
    a = 1
    b = 2
    return a+b
  
def function_b():
    c = 3
    return a+c
print(function_a())
print(function_b())