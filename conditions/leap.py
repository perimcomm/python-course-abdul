year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("leap")
elif year %4 == 0:
    print("leap")
else:
    print("not leap")