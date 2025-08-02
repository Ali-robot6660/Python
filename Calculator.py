a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
x = input("Enter an operator (+, -, *, /): ")

if x == "+":
    print(a + b)
elif x == "-":
    print(a - b)
elif x == "*":
    print(a * b)
elif x == "/":
    print(a / b)
else:
    print("Error operator")