numbers_of_numbers = int(input("Enter de quantity of numbers"))
counter = 0
sum = 0

while counter < numbers_of_numbers:
    n = int(input("Type a numbers: "))
    sum += n
    counter += 1

print("Sum is:", sum)