# Create a list is similar to array in other language
my_list =[]
print(my_list)
my_list =list()
print(my_list)
my_list =[1,2,3]
print(my_list)
my_list2 =["a","b","c"]
print(my_list2)
my_list3 =["a",1,"Python",5]
print(my_list3)

#Create a list from multiple lists
my_nested_list = [my_list,my_list2]
print(my_nested_list) 

#Extend the list
combo_list = []
one_list =[3,4]
combo_list.extend(my_list2)
print(combo_list)
# Easier way to add lists
my_list = [1,2,3]
my_list2 =["a","b","c"]
combo_list =my_list +my_list2
print(combo_list)
alpha_list = [34, 23, 67, 100, 88, 2]
print(alpha_list)
alpha_list.sort()
print(alpha_list)

# Tules are similar to list but tuple is immutable while the list is mutable
#create them with parentheses instead of square brackets
my_tuple =(1,2,3,4,5)
print(my_tuple[0:3])
another_tuple = tuple()
print(another_tuple)
abc = tuple([1, 2, 3])
print(abc)
#Dictionaries 
my_dict = {}
print(my_dict)
another_dict = dict()
print(another_dict)
my_other_dict = {"one":1, "two":2, "three":3}
print(my_other_dict)
print(my_other_dict["one"])
my_dict = {"name":"Mike", "address":"123 Happy Way"}
print(my_dict)
print(my_dict["name"])
print ("name" in my_dict)
print(my_dict.keys())
