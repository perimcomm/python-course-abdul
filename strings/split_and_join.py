s='a-b-c-d-e'
print(s.replace('-', ','))

s1='xyz'
s2='abc'
print(s1.join(s2))
s1='/'

print(s1.join(s2))

s1='-'
l1=['john', 'smith', 'ajay']

print(s1.join(l1))

s1='john smith ajay'

print(s1.split())

s1='john, smith, ajay'
print(s1.split(sep=',', maxsplit=1))
