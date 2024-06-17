list1=[1,2,3]
list2=[8,9,10]

list1.extend([4,5,6])
list2 = list2 + [11,12,13]
list1*2
print(list1)
list3= list1+list2

print(list3)

if 3 in list1:
    print('found')
else:
    print('not found')

if 7 not in list1:
    print('not found ')