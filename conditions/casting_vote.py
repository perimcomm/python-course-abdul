number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 < 0:
    x = (number1 * -1) - number2 
    print(x)
else: 
    x = number1 - number2
    print(x)