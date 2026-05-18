my_list = []

print("The list is currently empty:", my_list)

my_list.append("First item")
print("After adding the first item:", my_list)
my_list.append("Second item")
print("After adding the second item:", my_list)

# add items of different types
my_list.append(42)
print("After adding an integer:", my_list)
my_list.append(3.14)
print("After adding a float:", my_list)
my_list.append(True)
print("After adding a boolean:", my_list)
my_list.append("Another string")
print("After adding another string:", my_list)

# print list address
print("Memory address of my_list:", id(my_list))

# add number as string
my_list.append("100")
print("After adding a number as a string:", my_list)

# print list address again to show it has not changed
print("Memory address of my_list after adding '100':", id(my_list))

# type of list and members
print("The type of my_list is:", type(my_list))
print("The type of members of my_list are:")
for item in my_list:
    print(f"{item} is of type {type(item)}")

# change first item
my_list[0] = "Updated first item"
print("After updating the first item:", my_list)