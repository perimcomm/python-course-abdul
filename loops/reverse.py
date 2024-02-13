n = int(input("Type a number: "))
m = n
rev = 0

while n > 0:
    r = n % 10
    n = n // 10
    rev = rev * 10 + r

if m == rev:
    print("Palimdrome")
else:
    print("Not palimdrome")

