my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)

# delete multiple items
del my_list[1:4]  

# Output: ['p', 'm']
print(my_list)

my_list.clear()

# delete entire list
del my_list       

# Error: List not defined
print(my_list)