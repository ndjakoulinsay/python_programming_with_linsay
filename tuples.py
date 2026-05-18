fruits = ("apple", "banana", "cherry")
print(fruits)

print("The first fruit is:", fruits[0])
print("The second fruit is:", fruits[1])

# fruits[0] = "orange"  # This will raise a TypeError because tuples are immutable

# print tuple and address
print("Fruits tuple:", fruits)
print("Memory address of fruits tuple:", id(fruits))
# try to add a new fruit to the tuple
fruits = fruits + ("orange",)  
print("After adding orange:", fruits)
print("Memory address of fruits tuple after adding orange:", id(fruits))

# removing a fruit from the tuple is not possible, but we can create a new tuple without the unwanted fruit
fruits = fruits[:1] + fruits[2:]  # This will remove "banana"
print("After removing banana:", fruits)