<<<<<<< HEAD
# there are 2 type of loops for & while
# range function give range value
print(range(5))
#printing a range element using list
print(list(range(1,9,2)))
#for loop for in range
for number in range(5):
    print(number)
for number in [0,1,2,3,4]:
    print(number)
a_dict ={"one":1,"two":2,"three":3}
for key in a_dict:
    print(key)
a_dict ={1:"one",2:"two",3:"three"}
keys =a_dict.keys()
keys = sorted(keys)
for key in keys:
    print(key)

# finding even number in a range
numbers = int(input("Enter a number for range \n"))
for number in range(numbers):
    if number%2==0:
     print(number)

#while Loop
i =0
while i<10:
    print(i)
    i= i+1

#break statement
i =0
while i<10:
    print(i)
    if i==5:
        break
    i+=1
#continue statement

i =0
while i<10:
    if i==3:
        i+=1
        continue
    print(i)
    if i==5:
        break
    i+=1
=======
# there are 2 type of loops for & while
# range function give range value
print(range(5))
#printing a range element using list
print(list(range(1,9,2)))
#for loop for in range
for number in range(5):
    print(number)
for number in [0,1,2,3,4]:
    print(number)
a_dict ={"one":1,"two":2,"three":3}
for key in a_dict:
    print(key)
a_dict ={1:"one",2:"two",3:"three"}
keys =a_dict.keys()
keys = sorted(keys)
for key in keys:
    print(key)

# finding even number in a range
numbers = int(input("Enter a number for range \n"))
for number in range(numbers):
    if number%2==0:
     print(number)

#while Loop
i =0
while i<10:
    print(i)
    i= i+1

#break statement
i =0
while i<10:
    print(i)
    if i==5:
        break
    i+=1
#continue statement

i =0
while i<10:
    if i==3:
        i+=1
        continue
    print(i)
    if i==5:
        break
    i+=1
>>>>>>> 8170bb45957061d2afa628fa838bffb326cb527a
    