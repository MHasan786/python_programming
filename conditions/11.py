# Create a simple login system

username = input("Enter username ")
password = input("Enter password ")


correct_username = "Muhammad Hasan"
correct_password = "12345678"

if username == correct_username and password == correct_password:
    print("Login Sucessful Welcome,",correct_username)
else:
    print("Invalid username and password")