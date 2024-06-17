list1=[5,6,7,8,9]

for x in list1:
    print(x)

print('--------')
for i in range(len(list1)):
    print(list1[i])


print('--------')
for i in range (len(list1)-1,-1, -1):
    print(list1[i])

print('--------')

for i in range(-1, -(len(list1)+1), -1):
    print(list1[i])

print('--------')

y=0
while y < len(list1):
    print(list1[y])
    y=y+1

print('--------')


i = len(list1) + 1
print(i)
print(len(list1))

while i < len(list1):
    print(list1[i])
    i = i - 1
