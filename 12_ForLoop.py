print("Hello World!")

# Lets say we want to print this 5 times

for i in range(5):
    print("Hello World!")


for i in range(10):
    print(i)

for num in range(50, 100):
    print("Attempt ", num)


# We can also use the for loop to iterate through a list
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:
    print(fruit)


for i in range(1, 10, 2):
    print(i)


# Lets simulate a senerio where we send a message successfully

successful = False
for i in range(3):
    print("Attempt")
    if successful:
        print("Message sent successfully")
        break

    else:
        print("Message failed to send")
        print("Retrying...")
        print("Attempted 3 times but failed to send message")


# NESTED LOOPS

for x in range(5):
    for y in range(3):
        print(f"({x} , {y})")

# Iteration
for x in "Tanishq":
    print(x)
# same goes for lists

for x in [1, 2, 3, 4, 5]:
    print(x)
