n = int(input("Enter a number for factorial or power calculation: "))
vibor = input("Enter 'factorial' for factorial or 'power' for power calculation: ").lower()
result = 1
if vibor == 'factorial':
    for i in range(1, n + 1):
        result *= i
    print("Factorial number", n, "is", result)
elif vibor == 'power':
    power1 = int(input("Enter the power: "))
    for i in range(power1):
        result *= n
        print(n,"**", i+1, "=", result) #
else:
    print("Invalid input. Please enter 'factorial' or 'power'.")