temperature = 20
if temperature > 55:
    print("It's a hot day.")
elif temperature > 30:
    print("It's a warm day.")
else:
    print("It's not a hot day.")
print("DOne")


age = 21
if age >= 18:
    print("You are an adult.")

else:
    print("You are a minor.")


# More Cleaner Way to Write this

age = 21
message = "You are an adult." if age >= 18 else "You are a minor."
print(message)

