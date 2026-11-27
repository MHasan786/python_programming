# Check whether marks are between 50 and 100

marks1 = int(input("Enter a first number: "))
marks2 = int(input("Enter a first number: "))

between = marks1 >= 50 and marks2 <= 100
not_between = marks1 < 50 or marks2 > 100

print(f"Marks between 50 to 100 {between} or Marks not between 50 to 100 {not_between}")