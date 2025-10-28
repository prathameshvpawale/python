# write a python program to find a largest of time number using if -else statement take input from user .

num1 = float(input("enter number 1"))

num2 = float(input("enter number 2"))

num3 = float(input("enter number 3"))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"the largest number is {largest}")
