import random

n = random.randint(1, 10)
print(n)
guess = 0

while guess != n:
    guess = int(input("Type a number: "))
    if guess < n:
        print("It is lesser ")
    elif guess > n:
        print("It is larger")
    else:
        print("You guess the number")

print(guess)