# Accept marks of 5 subjects and display the student’s result according to the given conditions.

m1 = float(input("enter markss for subject 1 : "))
m2 = float(input("enter markss for subject 2 : "))
m3 = float(input("enter markss for subject 3 : "))
m4 = float(input("enter markss for subject 4 : "))
m5 = float(input("enter markss for subject 5 : "))

total = m1+m2+m3+m4+m5

percentage = total/5

if percentage >= 70:
    print("First Class with Distinction")
elif percentage >= 60:
    print("First class")
elif percentage >= 45:
    print("second class")
elif percentage >= 40:
    print("Pass")
else:
    print("Fail")
