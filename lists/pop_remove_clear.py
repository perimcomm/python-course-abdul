l1 = [5,6,7,8,9,10]

l1.pop()
l1.pop(0)
print(l1)

l1 = [5,6,7,8,9]

del l1[3]
print(l1)

l1 = [5,6,7,8,9,5,6,7,8,9]

l1.remove(6)
print(l1)
l1.remove(l1[-4])
print(l1)

l1.clear()
print(l1)


l1 = [5,6,7,8,9,10]
del l1[:]
print(l1)
