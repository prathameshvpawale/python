# Program to find GCD of two positive numbers

# Taking input from the user
num1 = int(input("Enter first positive number: "))
num2 = int(input("Enter second positive number: "))

# Make sure both numbers are positive
if num1 <= 0 or num2 <= 0:
    print("Please enter positive numbers only.")
else:
    # Find GCD using a loop
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1

    for i in range(1, smaller + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i

    print("The GCD of", num1, "and", num2, "is:", gcd)

