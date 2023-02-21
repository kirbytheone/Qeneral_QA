#  Task 3.1
names = "john peter brian Morgan Adam Maria bart";
print(names.title());
# print(names.upper())
# print(names.capitalized())

# Task 3.2
header_list = "Names"
friends_list =["John", "Marta", "James", "Amanda", "Marianna"];
header_list = header_list.center(45, "*")
print(header_list.upper())
for name in range(0,len(friends_list)):
    print(f'{friends_list[name]:>45}', sep="\n")

# Task 3.3 шото пока скипнул, not done
import ast
import json




"""
4 You have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"] 
convert it to a list of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]
"""
# Task 3.4 not done yet

veriable_names = ["FirstItem", "FriendsList", "MyTuple"]



#    if veriable.isupper():
#        snake = veriable.replace(veriable, f"_{veriable.lower()}")
#print(veriable)
# from camel_converter import to_snake
# to_snake(variable_names)