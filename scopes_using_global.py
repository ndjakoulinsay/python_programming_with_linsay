# global variable
name = "Linsay"

print(name)  # Output: Linsay

def who_are_you():
    global name  # This tells Python that we want to use the global variable 'name'
    name = "Ndjakou"
    print(name)  # Output: Ndjakou

who_are_you()
print(name)  # Output: Ndjakou