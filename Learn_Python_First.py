#Working With String
print("I'm a string ") #I'm a comment
#Creating a variable & storing String to It
my_string = "Welcome to Python!"
# Single Quote '' can also use to create string
another_string = 'The bright red fox jumped the fence.'
# Multiline Quote starts & Ends with '''   --Text--''' triple singline quotes 
a_long_string ='''This is a 
multiline string. It covers more than
one line'''
# Concatinating string using + operator
print(my_string +" : "+ another_string+ " : "+ a_long_string.strip())
# Storing a Interger & coverting it into string using str keyword
my_number = 123
# Convert No to String
my_string_number = str(my_number)
print(my_string_number)
#Converting a string into integer using int keyword
print( int("123"))
#ID used to for hecking id of the object
print(id(my_string))

#String are object in python
#String have methods also like uppercase,lowercase
print(my_string.upper())
print(my_string.lower())
print(my_string.strip())
#All string methods can be shown using dir
print(dir(my_string))
print(help(my_string.capitalize))
#checking data tyoe of 
print(type(my_string))
#String Slicing application
print(my_string[:1])
print(my_string[0:12])
print(my_string[0:13])
print(my_string[0:14])
print(my_string[0:-5])
print(my_string[:])
print(my_string[2:])
print(my_string[0])
#String formatting or Substitution application
string_1 ="I like %s" %"Python" #%s is a string variable and %"Python" is variable data to store
print(string_1)
var = "cookies"
newString ="I like %s and %s"%("Python",var)
print(newString)
# With Number
my_string = "%i + %i = %i" %(1,2,3)
print(my_string)
# with float
float_string = "%f" %(1.23)
print(float_string)
float_string = "%.2f" %(1.23)
print(float_string)
float_string = "%.2f" %(1.237)
print(float_string)
print("%(lang)s is fun!" %{"lang":"Python"})
my_string= "Python is as simple as {0}, {1},{2}".format("a","b","c")
print(my_string)
