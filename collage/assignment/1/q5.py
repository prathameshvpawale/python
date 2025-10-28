# Program to check whether a number is palindrome or not

num = int(input("Enter a number: "))

original = num

reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num = num // 10

if original == reverse:
    print(f"{original} is a Palindrome number.")
else:
    print(f"{original} is not a Palindrome number.")

