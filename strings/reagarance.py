s1 = input('enter a word: ')

lower=''
upper=''

for i in s1:
    if i.islower():
        lower = lower + i
    if i.isupper():
        upper = upper + i

print(lower+upper)