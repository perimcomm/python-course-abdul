s='python'

print(s.ljust(10))
print(s.rjust(10))
print(s.center(10,'*'))

s1='            python      '
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

s2='..... .... ++ aaapython'

print(s2.lstrip('.'))
print(s2.lstrip('. +'))
print(s2.lstrip('. +a'))