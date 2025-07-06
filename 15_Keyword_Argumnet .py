def increment(number, by):
    return number + by


result = increment(2, by=1)
print(result)  # Output: 3


# Default arguments
def increment(number, by=1):
    return number + by


result = increment(2)
print(result)  # Output: 3


# args , wait , what

def multiply(x, y):
    return x*y


result = multiply(2, 5)

print(result)  # Output: 10


# lets replace 2 paramenter with single paramenter

def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5, 6)


# Output: (2, 3, 4, 5, 6)

# lets iterate in loop

def multiply(* nums):
    total = 1
    for num in nums:
        total *= nums
        return total


print(multiply(2, 3, 4))
