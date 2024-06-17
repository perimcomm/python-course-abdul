l1 =[5,6,7,8]


print(l1)
l1.append(10)
print(l1)

#append using slices

l1[6:6] = [20]
l1[len(l1):] = [30]
print(l1)


l1.extend([10,11,12])
print(l1)

l1[len(l1):] = [30,31,32]
print(l1)

print(len(l1))

l1.insert(0, 99)
print(l1)

l2 = l1.copy()
l1.insert(12, 64)

print("printando duas listas")
print(f"lista 2: {l2}, \n lista1 {l1}")


l1[4:4] = [22]
print(l1)