#IF & Else Statement
var1 =3
var2 =2

if var1> var2:
    print("This is also True")
else:
    print("This is False")
#Take Input & ifelifelse
value = input("How much is that doggy in the window? ")
value = int(value)
 
if value<10:
    print("That's a great deal!")
elif 10<=value<=20:
    print("I'd still pay that...")
else:
    print("Wow! That's too much")
#Boolean Operator OR

x =10
y =0
if x<10 or y>15:
    print("This statement was True!")
else:
    print("No True")
#Boolean Operator AND
if x ==10 and y ==15:
    print("And Operation was True")
else:
    print("And is incorrect")
#Boolean Operator NOT
my_list = [1,2,3,4]
x = int(input("Enter a Number "))
if x not in my_list:
    print("'x' is not in the list, so this is true")
# Special Characters
# New line \n
print("I have an \n Newline in the middle")
# New Tab \t
print("I have an \tTabline in the middle")
# Print backslash \
print("This is a backslash\\")
