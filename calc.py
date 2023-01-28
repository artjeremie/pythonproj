# This function is used for adding two numbers
def add(P, Q):
    return P + Q


# This function is used for subtracting two numbers
def subtract(P, Q):
    return P - Q


# This function is used for multiplying two numbers
def multiply(P, Q):
    return P * Q


# This function is used for dividing two numbers
def divide(P, Q):
    return P / Q


# Now we will take inputs from the user
print("Please select operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/ b/ c/ d): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
    print("This is an invalid input")
