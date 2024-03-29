s1="Hello"
s2="world"

s3=s1+s2

print(len(s3))

for i in range(len(s3)-1, -1, -1):
    print(s3[i])

s3[0:]