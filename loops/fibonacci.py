n = int(input("Enter the fibonacci number: "))

first=0
second=1

for i in range(n+1):
    print(first)
    sol = first + second
    first = second
    second = sol

print(n)