# Create a grading system using marks.

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("You are grade is A+.")
elif marks >= 85 and marks < 90:
    print("You are grade is A.")
elif marks >= 75 and marks < 85:
    print("You are grade is B.")
elif marks >= 60 and marks < 75:
    print("You are grade is C.")
elif marks >= 50 and marks < 60:
    print("You are grade is D.")
else:
    print("You are grade is F.")