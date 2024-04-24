s = 'python is very easy'

print(s.startswith('py'))
print(s.startswith('is'))
print(s.startswith('is', 7))
print(s.endswith('easy'))
print(s.endswith('is', 0, 9))

print(s.partition('is'))
print(s.rpartition('y'))


j = 'python programming'

print(s.removeprefix('py'))
print(s.removeprefix('java'))
print(s.removesuffix('ing'))

