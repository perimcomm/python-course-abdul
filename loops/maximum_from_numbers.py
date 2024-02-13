numbers_of_numbers = int(input("Enter how much numbers do you want: "))
counter = 0 
max = int(input("Enter a number: "))

while counter < numbers_of_numbers - 1:
    n = int(input("Type number: "))
    if n > max:
        max = n
    counter += 1

print("The max numbers is: ", max)