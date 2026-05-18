students = ["Linsay", "Felix", "Alice", "Bob"]
print(students)
print("The first student is:", students[0])
print("The second student is:", students[1])

# add a student to the list
students.append("Charlie")
print("After adding Charlie:", students)
# removing a student from the list
students.remove("Alice")
print("After removing Alice:", students)
# add duplicate student to the list
students.append("Bob")
print("After adding Bob again:", students)
# count how many times Bob appears in the list
bob_count = students.count("Bob")
print("Bob appears", bob_count, "times in the list.")
# try removing Duplicate Bob
students.remove("Bob")
print("After removing Bob once:", students)

# copy list of students
students_copy = students.copy()
print("Copied list of students:", students_copy)
# clear the original list of students
students.clear()
print("Original list after clearing:", students)
print("Copied list remains unchanged:", students_copy)