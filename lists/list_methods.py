L1 = [
    5,7,8,9,5,8,9,10,6
    ]

L1.index(8)
print(L1.index(8, 3))
#print(L1.index(8, 0, 1))
print(L1.count(9))
L1.reverse()
print(L1)
L1.sort()
print(L1)
L1.sort(reverse=True)
print(L1)

L2 = [ "yy", "jj", "mm", "BB", "aa", "ZZ"]
L2.sort()
print(L2)
L2.sort(key=str.lower)
print(L2)
L2.sort(key=str.lower, reverse=True)
print(L2)

print(sorted(L2))