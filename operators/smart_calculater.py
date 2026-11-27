# Smart Simple Calculater

print("===== SMART CALCULATOR =====")


first_num = float(input("Enter first number: "))
operator = input("Enter operator from this + - x / ** // %: ")
second_num = float(input("Enter second number: "))

if operator == "+":
    result = first_num + second_num
    print("Result: ",result)
elif operator == "-":
    result = first_num - second_num
    print("Result: ",result)
elif operator == "x":
    result = first_num * second_num
    print("Result: ",result)
elif operator == "/":
    if second_num != 0:
        result = first_num /second_num
        print("Result: ",result)
    else:
        print("Error: Can not divided by zero.")
elif operator == "**":
    result1 = first_num ** 2
    result2 = second_num ** 2
    print(f"Power of first number: {result1}\nPower of second number: {result2}")
elif operator == "//":
    if second_num != 0:
        result = first_num // second_num
        print("Result: ",result)
    else:
        print("Error: Can not divided by zero.")
elif operator == "%":
    if second_num != 0:
        result = first_num % second_num
        print("Result: ",result)
    else:
        print("Error: Can not divided by zero.")
else:
    print("Invalid operator")



