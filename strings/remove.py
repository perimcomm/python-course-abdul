punctuation = "_ . - @"
print(punctuation)


'''
bruno-bidas@lalala.com
'''
s1 = input("enter a word: ")
s2 = ''

for i in s1:
    if i not in punctuation:
        s2 = s2 + i

print(s2)