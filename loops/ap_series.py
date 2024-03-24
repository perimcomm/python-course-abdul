a = int(input("Enter how much terms: "))
d = int(input("Enter the number that you want start: "))
n = int(input("Enter the difference between numbers: "))

for i in range(a, a + n * d, d):
    print(i)