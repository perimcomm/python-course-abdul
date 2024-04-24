palavra = input("Enter a string: ")

tamanho= len(palavra)
rev = palavra[:: -1]

print(palavra[:tamanho:])


if palavra[0::] == palavra[::-1 ]:
    print("it is a palindrome")
else:
    print("not palimdrome")

print(palavra+rev)