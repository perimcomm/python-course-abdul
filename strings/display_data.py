name=str(input("Digite o nome do produto: "))
price=str(input("Digite o preço: "))

sumlen = len(name) + len(price)
dots = '.' * (25 - sumlen)

print(name+dots+price)

    