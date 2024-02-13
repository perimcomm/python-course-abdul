counter = 0
number = int(input("Digite um numero: "))

while number > 0:
    number = number // 10
    counter += 1
    

print(counter)