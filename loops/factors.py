n = int(input("Enter a number: "))

for i in range(1, n+1):
    if n % i == 0:
        print(f"Number: {i} is factorial of {n}")
    else: 
         print(f"Number: {i} is not factorial of {n}")