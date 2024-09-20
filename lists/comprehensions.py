L1 = [x for x in range(10)]
L2 = [x**2 for x in range(1,6)]
L3 = [ x for x in (10,5,7,8,12,3) if x % 2 == 0 ]
L4 = [x.lower() for x in 'Python']
L5 = [ x for x in "abc12d3-&fg4$hi2" if x.isalpha()]

L7 = input("Enter names: ").split()

print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(L7)