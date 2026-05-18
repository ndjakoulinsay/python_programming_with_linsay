# empty dictionary
my_dict = {}
print("The dictionary is currently empty:", my_dict)
# add key-value pairs to the dictionary
my_dict["name"] = "Alice"
print("After adding name:", my_dict)
my_dict["age"] = 30
print("After adding age:", my_dict)
my_dict["city"] = "New York"
print("After adding city:", my_dict)
# update a value in the dictionary
my_dict["age"] = 31
print("After updating age:", my_dict)
# add a duplicate key to the dictionary (this will overwrite the existing value)
my_dict["name"] = "Bob"
print("After adding duplicate name key:", my_dict)
# check if a key is in the dictionary 
print("Is 'name' in the dictionary?", "name" in my_dict)
# get the value associated with a key
print("The name in the dictionary is:", my_dict["name"])
# get the value of a key that does not exist (this will raise a KeyError)
try:
    print(my_dict["nonexistent_key"])  # Uncommenting this line will raise a KeyError
except KeyError:
    print("Key not found")
# use the get method to avoid KeyError
print("Using get method for nonexistent key:", my_dict.get("nonexistent_key", "Key not found"))
# use get without default value (this will return None)
print("Using get method without default value:", my_dict.get("nonexistent_key"))

keys = my_dict.keys()
print("Keys in the dictionary:", keys, "Type:", type(keys))
values = my_dict.values()
print("Values in the dictionary:", values, "Type:", type(values))

# iterate over keys and print
print("Iterating over keys:")
for key in keys:
    print(key)

# interate over values and print
print("Iterating over values:")
for value in values:
    print(value)

# printing dictionary using []
print("Dictionary using []:", my_dict)
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

# printing dictionary using get()
print("Dictionary using get():")
for key in my_dict:
    print(f"{key}: {my_dict.get(key)}")

# priting dictionary using items()
print("Dictionary using items():")
for key, value in my_dict.items():
    print(f"{key}: {value}")