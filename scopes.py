# global variable
name = "Linsay"

print(name)  # Output: Linsay

def who_are_you():
    name = "Ndjakou"
    print(name)  # Output: Ndjakou
    if name == "Ndjakou":
        another_name = "Audrey"
        print(another_name)  # Output: Audrey
    print(another_name)  # Output: Audrey

who_are_you()
print(name)  # Output: Linsay
# print(another_name)  # This will raise an error because another_name is not defined in this scope