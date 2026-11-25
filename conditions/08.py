# Create a simple calculator.

n1 = float(input("Enter a first number: "))
n2 = float(input("Enter a second number: "))
symbol = str(input("Enter symbol to you required opration: "))

if symbol == "+":
    print(n1 + n2)
elif symbol == "-":
    print(n1 - n2)
elif symbol == "x":
    print(n1 * n2)
elif symbol == "/":
    print(n1 / n2)
elif symbol == "%":
    print(n1 % n2)