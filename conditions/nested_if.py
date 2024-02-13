john = int(input("Enter john age: "))
smith = int(input("Enter smith age: "))
ajay = int(input("Enter ajay age: "))

if john > smith and john > ajay:
    print("John is oldest")
elif smith > ajay:
    print("Smith is oldest")
else:
    print("Ajay is oldest")