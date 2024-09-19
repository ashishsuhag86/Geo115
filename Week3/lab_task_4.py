# Nested If-Else Statements Example: Age Category
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

# Multiple Conditions Example: Positive, Negative, or Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

# Boolean Operations Example: Valid Email
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email address")
else:
    print("Invalid email address")
