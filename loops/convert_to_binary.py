n = int(input(" Type a number: "))

binary = ""

while n > 0:
    r = n % 2
    n = n // 2
    binary = str(r) + binary


print(binary)
