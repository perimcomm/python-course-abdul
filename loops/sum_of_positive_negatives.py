numbers_of_numbers = int(input("Enter de quantity of numbers"))
counter = 0
psum = 0
nsum = 0

while counter < numbers_of_numbers:
    n = int(input("Type a numbers: "))
    if n < 0:
        nsum += n
    elif n > 0:
        psum += n
    counter += 1

print(f"Positive sum is and negative sum is ", (psum, nsum))