
# University Admission Eligibility Checker

print("===== UNIVERSITY ADMISSION CHECKER =====")

# Admission requirements
REQUIRED_MARKS = 770
TOTAL_MARKS = 1100
MINIMUM_AGE = 17

# Get student information
year_passed = int(input("Enter your passing class (12 for Intermediate): "))

if year_passed == 12:

    marks_obtained = int(input("Enter your obtained marks: "))
    age = int(input("Enter your age: "))

    # Validate marks
    if marks_obtained < 0 or marks_obtained > TOTAL_MARKS:
        print("Invalid marks! Please enter marks between 0 and 1100.")

    elif age <= 0:
        print("Invalid age! Please enter a valid age.")

    # Check admission eligibility
    elif marks_obtained >= REQUIRED_MARKS and age >= MINIMUM_AGE:
        print("\nCongratulations! You are eligible for university admission.")
        print(f"Your Marks: {marks_obtained}/{TOTAL_MARKS}")
        print(f"Your Age: {age}")

    else:
        print("\nSorry! You are not eligible for university admission.")

        if marks_obtained < REQUIRED_MARKS:
            print("Reason: You need at least 770 marks.")

        if age < MINIMUM_AGE:
            print("Reason: Your age must be at least 17 years.")

else:
    print("You must pass 12th class before applying for university admission.")
