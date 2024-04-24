bin = input('Enter your credit card number: ')

lastdigits = bin[15::]

four = '*' * 4 + ' '

dispno = four * 3 + lastdigits

print(dispno)