n = int(input("Digite um numero: "))
sum = 0
while n > 0:
    r = n % 10
    n = n // 10
    sum += r

print(sum)