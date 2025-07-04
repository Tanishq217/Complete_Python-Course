course = "Python for Beginnerss"
message = "Hello World"

# length of string

print(len(course))  # Output: 21

# Accessing characters in a string
print(course[0])
print(course[-3])  # Output: P

# Slicing strings
print(course[0:3])  # Output: Pyt

print(course[0:])   # Output: Python for Beginnerss


print(course[:3])   # Output: Pyt


# Problem with Double   Quotes

course2 = "Python \" for Beginnerss"
print(course2)  # Output: Python " for Beginnerss

# Adding new line
course3 = "Python \n for Beginnerss"
print(course3)  # Output: Python
# for Beginnerss

# CONCATENATION

first = "Python"
last = "for Beginnerss"
full = first + " " + last
print(full)  # Output: Python for Beginnerss

# Better way to concatenate strings
full2 = f"{first} {last}"

# Function for Strings

name = "tanishq Singh"
upper_name = name.upper()  # Output: TANISHQ SINGH
lower_name = name.lower()  # Output: tanishq singh
title_name = name.title()  # Output: Tanishq Singh
print(upper_name)
print(lower_name)
print(title_name)


name_with_space = "            Tanishq Singh Boss     "

print(name_with_space.strip())  # Output: Tanishq Singh
# rstrip and lstrip


# Finding Boss
print(name_with_space.find("Boss"))  # Output: 15

# Output:             Tanishq Singh King
print(name_with_space.replace("Boss", "King"))


print(name_with_space.find("Bossssss"))
# Output: -1 (not found)

# in expression
print("Boss" in name_with_space)  # Output: True
print("Boss" not in name_with_space)  # Output: False
