# Practical Exercise: Student Information System
# Project requirements
# Create a program that asks a student for:
# 1. Full name.
# 2. Age.
# 3. Roll number.
# 4. City.
# 5. Marks in English.
# 6. Marks in Mathematics.
# 7. Marks in Computer Science.
# Then calculate:
# - Total marks.
# - Average marks.
# - Percentage (assuming each subject is out of 100).
print("==================================")
print("       STUDENT INFORMATION        ")
print("==================================")

stu_name = str(input("Enter your name here: "))
stu_age = int(input("Enter your age: "))
stu_roll_no = int(input("Enter your roll no: "))
stu_city = str(input("Enter your city name: "))
marks_eng = int(input("Enter your marks in English: "))
marks_math = int(input("Enter your marks in Math: "))
marks_cs = int(input("Enter your marks in Computer Science: "))

total_marks = 300
given_marks = marks_eng + marks_math + marks_cs
avg_marks = round(given_marks / 3,2)
per_marks = round((given_marks / total_marks) * 100,2)

print("==================================")
print("       STUDENT REPORT        ")
print("==================================")

print("Name: ",stu_name)
print("Age :",stu_age)
print("Roll No: ",stu_roll_no)
print("City: ",stu_city)
print("Marks in English: ",marks_eng)
print("Marks in Math: ",marks_math)
print("Marks in Computer Science: ",marks_cs)

print("Marks Obtained: ",given_marks)
print("Avrage of Marks: ", avg_marks)
print("Percentage of Marks: ", per_marks)