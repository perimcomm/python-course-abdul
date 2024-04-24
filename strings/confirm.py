passwd = input('Enter password:')
repasswd = input('Enter password again')

if passwd.casefold() != repasswd.casefold():
    print("Check the password typed")

